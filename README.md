**中文** | [English](README_EN.md)

# Fable 5.5 Testing Series — Claude Fable 5.5 实测案例索引

收集 X (Twitter) 上关于 **Claude Fable 5.5** 的单句提示词动画、3D 与交互测试案例：链接、提示词、耗时与成本、结果亮点，一处索引。

> **注意**：截至 2026 年 11 月，Fable 5.5 尚未被 Anthropic 官方发布。以下均为早期访问/路由报告，请以原帖为准。
> 本仓库仅做整理与索引；每条案例的预览为原视频前 5 秒的 WebP 动图，完整内容请看原帖。原帖与视频版权归各原作者所有。

> 💡 **如何贡献**：在本仓库提交 [Issue](../../issues/new?template=submit_case.yml)（模板会自动带 `submission` 标签），只需粘贴一条推文链接，GitHub Actions 会自动解析、分类并更新本页与 `data/cases.json`。

## 总览表

| 预览 | Part | 标题 | 作者 | 耗时 | 成本 | 时长 | 日期 | 原帖 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <img src="assets/previews/2117666378174050352.webp" width="160" /> | 初始 | Clockwork Bird（发条鸟） | @camperaigg | 1h54m | ~$20 | 60s | 2026-11-03 | [链接](https://x.com/camperaigg/status/2117666378174050352) |
| <img src="assets/previews/2117694354685092255.webp" width="160" /> | Part 2 | Link's Master Sword | @camperaigg | 32min+ | $11.66 | 34s | 2026-11-03 | [链接](https://x.com/camperaigg/status/2117694354685092255) |
| <img src="assets/previews/2117717189059026969.webp" width="160" /> | Part 3 | Anime Stickman Sword Fight | @camperaigg | 66min | $15.71 | 46s | 2026-11-03 | [链接](https://x.com/camperaigg/status/2117717189059026969) |
| <img src="assets/previews/2117914482752299311.webp" width="160" /> | Part 4 | Transformer Truck | @camperaigg | 107min | $9.64 | 12.5s | 2026-11-04 | [链接](https://x.com/camperaigg/status/2117914482752299311) |
| <img src="assets/previews/2117966825048997914.webp" width="160" /> | Part 5 | Howl's Moving Castle | @camperaigg | 133min | $12.37 | 35s | 2026-11-04 | [链接](https://x.com/camperaigg/status/2117966825048997914) |
| <img src="assets/previews/2118002649929056373.webp" width="160" /> | Part 6 | Mechanical Heart | @camperaigg | 106min | $12.35 | 30s | 2026-11-04 | [链接](https://x.com/camperaigg/status/2118002649929056373) |
| <img src="assets/previews/2118069524306284556.webp" width="160" /> | Part 7 | Whale Breach | @camperaigg | 154min | $17.85 | 31s | 2026-11-04 | [链接](https://x.com/camperaigg/status/2118069524306284556) |
## 🎬 动画与视频生成 (Video & Animation)

| 预览 | 案例名称与摘要 | 技术栈 & 状态 | 原始 Prompt / 链接 |
| :--- | :--- | :--- | :--- |
| <img src="assets/previews/2117666378174050352.webp" width="220" /> | **Clockwork Bird（发条鸟）**<br/>全矢量发条鸟自动组装成片，原创华尔兹与纯数学合成音效贯穿。<br/>*By @camperaigg (2026-11-03)* | `Claude Code` `HyperFrames`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2117666378174050352)<br/><details><summary>查看 Prompt</summary><pre>一句提示词（未公开完整原文）</pre></details> |
| <img src="assets/previews/2117694354685092255.webp" width="220" /> | **Link's Master Sword**<br/>单脚本在 Blender 中建模大师之剑并自动成片，附原创管弦乐。<br/>*By @camperaigg (2026-11-03)* | `Claude Code` `Blender`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2117694354685092255)<br/><details><summary>查看 Prompt</summary><pre>Build Link's Master Sword in Blender（后续追加“make a video of it”）</pre></details> |
| <img src="assets/previews/2117717189059026969.webp" width="220" /> | **Anime Stickman Sword Fight**<br/>动漫风火柴人剑斗：布料模拟、冲击闪与 228 个物理同步音效。<br/>*By @camperaigg (2026-11-03)* | `Claude Code`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2117717189059026969)<br/><details><summary>查看 Prompt</summary><pre>Make me a video of 2 stickman fighting, anime style.</pre></details> |
| <img src="assets/previews/2117914482752299311.webp" width="220" /> | **Transformer Truck**<br/>51 关节绑定变形卡车，雨幕涟漪与纯合成机械音效。<br/>*By @camperaigg (2026-11-04)* | `Claude Code` `Blender`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2117914482752299311)<br/><details><summary>查看 Prompt</summary><pre>Make me a transformer truck with animations of its transforming.</pre></details> |
| <img src="assets/previews/2117966825048997914.webp" width="220" /> | **Howl's Moving Castle**<br/>会行走的城堡：蒸汽机到四足步态全建模，中途开壳剖视。<br/>*By @camperaigg (2026-11-04)* | `Claude Code` `Blender`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2117966825048997914)<br/><details><summary>查看 Prompt</summary><pre>Make me Howl's moving castle and also show its internal machinery.</pre></details> |
| <img src="assets/previews/2118002649929056373.webp" width="220" /> | **Mechanical Heart**<br/>机械心脏开壳动画：双活塞曲轴与心跳同步配乐。<br/>*By @camperaigg (2026-11-04)* | `Claude Code` `Blender`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2118002649929056373)<br/><details><summary>查看 Prompt</summary><pre>Make a mechanical heart and show its insides, use blender.</pre></details> |
| <img src="assets/previews/2118069524306284556.webp" width="220" /> | **Whale Breach**<br/>1690 万粒子流体与 cel-shading 海洋，鲸鱼跃水成片。<br/>*By @camperaigg (2026-11-04)* | `Claude Code`<br/>🏷️ 实测验证 | [🔗 原推文](https://x.com/camperaigg/status/2118069524306284556)<br/><details><summary>查看 Prompt</summary><pre>Make a whale breach a cel-shaded ocean.</pre></details> |
## 详细记录
### 初始：Clockwork Bird（发条鸟）
- **原帖**：[https://x.com/camperaigg/status/2117666378174050352](https://x.com/camperaigg/status/2117666378174050352) · **耗时**：1h54m · **成本**：~$20 · **时长**：60s- **提示词**：一句提示词（未公开完整原文）
- **亮点**：全矢量发条鸟零件飞入组装、连续镜头；原创华尔兹贯穿全片；纯数学合成音效（点击与帧精确同步 ±5ms）
### Part 2：Link's Master Sword
- **原帖**：[https://x.com/camperaigg/status/2117694354685092255](https://x.com/camperaigg/status/2117694354685092255) · **耗时**：32min+ · **成本**：$11.66 · **时长**：34s- **提示词**：Build Link's Master Sword in Blender（后续追加“make a video of it”）
- **亮点**：单脚本完整建模（Triforce 浮雕、编织握把、多层羽毛护手）；自动修复 z-fighting；连续运镜 + 森林光影 + 原创管弦乐
### Part 3：Anime Stickman Sword Fight
- **原帖**：[https://x.com/camperaigg/status/2117717189059026969](https://x.com/camperaigg/status/2117717189059026969) · **耗时**：66min · **成本**：$15.71 · **时长**：46s- **提示词**：Make me a video of 2 stickman fighting, anime style.
- **亮点**：骨骼 + 120Hz 布料、闪电刀 vs 火焰大剑；一帧冲击闪（mono/inverted/duotone）；16 乐器 120BPM 原创配乐；228 个物理同步音效（其中 79 个自动从剑尖速度检测）；高潮前全静音
### Part 4：Transformer Truck
- **原帖**：[https://x.com/camperaigg/status/2117914482752299311](https://x.com/camperaigg/status/2117914482752299311) · **耗时**：107min · **成本**：$9.64 · **时长**：12.5s- **提示词**：Make me a transformer truck with animations of its transforming.
- **亮点**：51 关节完整绑定 + 地面求解；Geometry Nodes 雨滴与涟漪；64 个纯合成音效（柴油/气刹/舵机等）
### Part 5：Howl's Moving Castle
- **原帖**：[https://x.com/camperaigg/status/2117966825048997914](https://x.com/camperaigg/status/2117966825048997914) · **耗时**：133min · **成本**：$12.37 · **时长**：35s- **提示词**：Make me Howl's moving castle and also show its internal machinery.
- **亮点**：完整蒸汽机→齿轮系→四足行走（从着地脚反解）；中途开壳剖视；步频精确华尔兹（1.4s/拍）；自动发现并优化草渲染（9.3s→4.2s/帧）
### Part 6：Mechanical Heart
- **原帖**：[https://x.com/camperaigg/status/2118002649929056373](https://x.com/camperaigg/status/2118002649929056373) · **耗时**：106min · **成本**：$12.35 · **时长**：30s- **提示词**：Make a mechanical heart and show its insides, use blender.
- **亮点**：双活塞曲轴、开壳动画；黄金油液气泡与滴落；心跳同步配乐；自动排查隐藏灯光问题
### Part 7：Whale Breach
- **原帖**：[https://x.com/camperaigg/status/2118069524306284556](https://x.com/camperaigg/status/2118069524306284556) · **耗时**：154min · **成本**：$17.85 · **时长**：31s- **提示词**：Make a whale breach a cel-shaded ocean.
- **亮点**：1690 万粒子流体（1200 steps/s）；三层 FFT 波浪 + cel-shading；109 万三角纯代码鲸鱼；水下光学（Snell's window）；自动发现并重渲染交叉线问题
## 相关资源
- 其他 Fable 5.5 社区合集：[awesome-fable5-5-videos](https://github.com/billyhetech/awesome-fable5-5-videos)、[awesome-fable-5.5-usecase](https://github.com/coolbat/awesome-fable-5.5-usecase)

## 说明与版权
- 所有视频与描述均来自各原作者的公开推文，请以原帖为准。
- 本仓库的整理与索引部分以 [MIT License](LICENSE) 发布；索引所指向的原帖内容与视频版权归原作者所有。
- 种子案例为 @camperaigg 的 Fable 5.5 Testing Series（Part 1–7）。
