#!/usr/bin/env python3
"""Render README.md from data/cases.json using templates/README.md.j2."""
import json

from jinja2 import Environment, FileSystemLoader

CATEGORIES = {
    "video_gen": "🎬 动画与视频生成 (Video & Animation)",
    "interactive_h5": "📱 交互式 H5 与微应用 (Interactive H5 & Apps)",
    "game_physics": "🎮 网页小游戏与物理模拟 (Games & Physics)",
    "shader_ui": "🎨 前端 UI 与 Shader 特效 (UI & Shaders)",
}


def cell(value) -> str:
    """Sanitize a value for use inside a Markdown table cell."""
    if value is None:
        return ""
    return str(value).replace("|", "¦").replace("\n", " ").strip()


def cost(value) -> str:
    """Format a cost value: 11.66 -> $11.66, '~20' -> ~$20, '' -> ''."""
    if value is None or value == "":
        return ""
    if isinstance(value, (int, float)):
        return f"${value:g}" if float(value) % 1 else f"${value}"
    s = str(value).strip()
    if s.startswith("~"):
        return "~$" + s[1:]
    if "$" in s:
        return s
    return "$" + s


def build():
    with open("data/cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["cell"] = cell
    env.filters["cost"] = cost
    template = env.get_template("README.md.j2")
    md = template.render(cases=cases, categories=CATEGORIES)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md)
    print(f"README.md rendered from {len(cases)} cases.")


if __name__ == "__main__":
    build()
