#!/usr/bin/env python3
"""Auto-ingest a Fable 5.5 test tweet into data/cases.json.

Pipeline: FxTwitter public API (metadata + direct media links) ->
optional media download + WebP preview (yt-dlp, direct-URL fallback) ->
optional LLM structured extraction -> append to data/cases.json.

Environment:
  TWEET_URL    (required) https://x.com/<author>/status/<id>
  USER_NOTES   (optional) free-text notes / prompt supplied by the submitter
  LLM_API_KEY  (optional) if unset, a basic record is built from metadata
  LLM_BASE_URL (optional, default https://api.openai.com/v1)
  LLM_MODEL    (optional, default gpt-4o-mini)

Note: preview generation downloads the original video and stores a short
(5s) WebP derivative in assets/previews/. The repository owner has accepted
this republication scope; all entries keep author attribution and link back
to the original post.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime

import requests

CASES_FILE = "data/cases.json"
PREVIEW_DIR = "assets/previews"

CATEGORIES = {
    "video_gen": "🎬 动画与视频生成",
    "interactive_h5": "📱 交互式 H5 与微应用",
    "game_physics": "🎮 网页小游戏与物理模拟",
    "shader_ui": "🎨 前端 UI 与 Shader 特效",
}


def extract_tweet_ref(url: str):
    match = re.search(r"(?:twitter\.com|x\.com)/([^/]+)/status/(\d+)", url or "")
    if not match:
        raise ValueError(f"无效的推文链接: {url}")
    return match.group(1), match.group(2)


def fetch_tweet_metadata(author: str, tweet_id: str) -> dict:
    """Fetch tweet text/author/media via the FxTwitter public API."""
    api_url = f"https://api.fxtwitter.com/{author}/status/{tweet_id}"
    resp = requests.get(api_url, timeout=20)
    resp.raise_for_status()
    data = resp.json().get("tweet", {})

    created_at = ""
    raw_date = data.get("created_at", "")
    if raw_date:
        try:
            created_at = datetime.strptime(
                raw_date, "%a %b %d %H:%M:%S %z %Y"
            ).strftime("%Y-%m-%d")
        except ValueError:
            created_at = ""

    media_urls = [
        m.get("url")
        for m in (data.get("media") or {}).get("all", [])
        if m.get("type") in ("video", "gif") and m.get("url")
    ]
    duration_sec = None
    for m in (data.get("media") or {}).get("all", []):
        if m.get("type") == "video" and m.get("duration"):
            duration_sec = m["duration"]
            break

    return {
        "text": data.get("text", ""),
        "author": f"@{data.get('author', {}).get('screen_name', author)}",
        "media_urls": media_urls,
        "duration_sec": duration_sec,
        "created_at": created_at,
    }


def _to_webp(mp4_path: str, webp_path: str) -> bool:
    cmd = [
        "ffmpeg", "-y", "-v", "error", "-i", mp4_path,
        "-t", "5",
        "-vf", "fps=12,scale=480:-1:flags=lanczos",
        "-vcodec", "libwebp", "-lossless", "0", "-compression_level", "6",
        "-q:v", "65", "-loop", "0", "-an",
        webp_path,
    ]
    subprocess.run(cmd, check=True)
    return os.path.exists(webp_path)


def download_and_convert_media(tweet_url: str, tweet_id: str, direct_url: str = "") -> str:
    """Download the tweet video and convert the first 5s to a WebP preview."""
    os.makedirs(PREVIEW_DIR, exist_ok=True)
    mp4_path = f"/tmp/{tweet_id}.mp4"
    webp_path = f"{PREVIEW_DIR}/{tweet_id}.webp"

    got = False
    try:
        subprocess.run(
            ["yt-dlp", "-f", "best[ext=mp4]", "-o", mp4_path, tweet_url],
            check=True, capture_output=True, timeout=300,
        )
        got = os.path.exists(mp4_path)
    except Exception as e:
        print(f"yt-dlp 下载失败，尝试直链: {e}")
    if not got and direct_url:
        r = requests.get(direct_url, timeout=300)
        r.raise_for_status()
        with open(mp4_path, "wb") as f:
            f.write(r.content)
        got = os.path.exists(mp4_path)
    if not got:
        raise RuntimeError("视频下载失败")
    if not _to_webp(mp4_path, webp_path):
        raise RuntimeError("WebP 转码失败")
    return webp_path


def analyze_with_llm(tweet_text: str, user_notes: str = "") -> dict:
    """Structured extraction with an OpenAI-compatible LLM endpoint."""
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ["LLM_API_KEY"],
        base_url=os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1"),
    )
    system_prompt = """你是一个开源项目整理助手，负责整理关于 Claude Fable 5.5 的测试案例。
请根据推文内容提取以下 JSON 字段（严格输出合法 JSON）：
- category: 只能是 ["video_gen", "interactive_h5", "game_physics", "shader_ui"] 之一
- category_name: 对应 ["🎬 动画与视频生成", "📱 交互式 H5 与微应用", "🎮 网页小游戏与物理模拟", "🎨 前端 UI 与 Shader 特效"]
- title: 简短有吸引力的中文标题（15字以内）
- summary: 一句话中文摘要，说明测试效果与亮点（40字以内）
- title_en: 对应的英文标题（8个词以内）
- summary_en: 对应的一句英文摘要（25个词以内）
- prompt: 提取推文中提到的原始 Prompt（若无则填 "未公开"）
- tech_stack: 数组，提取涉及的技术栈如 ["Three.js", "HTML5", "Canvas", "Remotion"]
- demo_url: 推文中包含的在线预览链接（若无则填 ""）
- verification: 判断属于 "实测验证" 还是 "灰度路由/传闻"
"""
    response = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL", "gpt-4o-mini"),
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"推文内容:\n{tweet_text}\n\n补充说明:\n{user_notes}"},
        ],
    )
    content = response.choices[0].message.content
    # Some providers return content as a list of parts instead of a string.
    if isinstance(content, list):
        content = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )
    parsed = json.loads(content)
    # Some models wrap the object in a one-element JSON array.
    if isinstance(parsed, list):
        parsed = next((x for x in parsed if isinstance(x, dict)), {})
    return parsed


def fallback_record(meta: dict, user_notes: str) -> dict:
    """Used when LLM_API_KEY is not configured: keep the pipeline working."""
    if "### " in (user_notes or ""):
        # Raw issue-form dump, not real notes — don't leak form scaffolding
        # into the record.
        user_notes = ""
    first_line = (meta["text"] or "").strip().split("\n")[0][:40]
    return {
        "category": "video_gen",
        "category_name": CATEGORIES["video_gen"],
        "title": first_line or "Fable 5.5 测试案例",
        "summary": (meta["text"] or "")[:60],
        "title_en": first_line or "Fable 5.5 test case",
        "summary_en": (meta["text"] or "")[:120],
        "prompt": user_notes or "未公开",
        "tech_stack": [],
        "demo_url": "",
        "verification": "灰度路由/传闻",
    }


def ingest_case(tweet_url: str, user_notes: str = "") -> dict | None:
    """Ingest one tweet into data/cases.json. Returns the new case, or None
    if the tweet is already indexed. Raises on unrecoverable fetch errors
    so batch callers can skip the tweet and continue."""
    author, tweet_id = extract_tweet_ref(tweet_url)

    with open(CASES_FILE, "r", encoding="utf-8") as f:
        cases = json.load(f)
    if any(c["id"] == tweet_id for c in cases):
        print(f"推文 {tweet_id} 已存在，跳过处理。")
        return None

    meta = fetch_tweet_metadata(author, tweet_id)

    preview_webp = ""
    if meta["media_urls"]:
        try:
            preview_webp = download_and_convert_media(
                tweet_url, tweet_id, meta["media_urls"][0]
            )
        except Exception as e:
            print(f"媒体处理失败，降级为纯文本收录: {e}")

    if os.environ.get("LLM_API_KEY"):
        try:
            llm_data = analyze_with_llm(meta["text"], user_notes)
        except Exception as e:
            print(f"LLM 解析失败，降级为基础记录: {e}")
            llm_data = fallback_record(meta, user_notes)
    else:
        print("未配置 LLM_API_KEY，使用基础记录（请在仓库 Secrets 中添加后获得完整分类）。")
        llm_data = fallback_record(meta, user_notes)

    if llm_data.get("category") not in CATEGORIES:
        llm_data["category"] = "video_gen"
        llm_data["category_name"] = CATEGORIES["video_gen"]

    # Never let a missing LLM field crash ingestion downstream.
    first_line = (meta["text"] or "").strip().split("\n")[0][:40]
    if not llm_data.get("title"):
        llm_data["title"] = first_line or "Fable 5.5 测试案例"
    if not llm_data.get("summary"):
        llm_data["summary"] = (meta["text"] or "")[:60]
    if not llm_data.get("title_en"):
        llm_data["title_en"] = llm_data["title"]
    if not llm_data.get("summary_en"):
        llm_data["summary_en"] = llm_data["summary"]

    new_case = {
        "id": tweet_id,
        "tweet_url": tweet_url,
        "author": meta["author"],
        **llm_data,
        "preview_webp": preview_webp,
        "video_url": "",
        "demo_url": llm_data.get("demo_url", ""),
        "duration_sec": meta["duration_sec"],
        "work_time": "",
        "cost_usd": "",
        "highlights": [],
        "created_at": meta["created_at"] or datetime.now().strftime("%Y-%m-%d"),
    }

    cases.insert(0, new_case)
    with open(CASES_FILE, "w", encoding="utf-8") as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)
    print(f"成功收录案例: {new_case.get('title', '')}")
    return new_case


def main() -> int:
    tweet_url = os.environ.get("TWEET_URL", "").strip()
    user_notes = os.environ.get("USER_NOTES", "").strip()
    if not tweet_url:
        print("TWEET_URL 为空，跳过。")
        return 0
    ingest_case(tweet_url, user_notes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
