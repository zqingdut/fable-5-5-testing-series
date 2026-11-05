# Fable 5.5 Testing Series by @camperaigg

> 社区整理：@camperaigg（camper 🦎🎣）使用 Claude Fable 5.5（Xhigh / Claude Code）进行的单句提示词动画与 3D 测试合集。
> **注意**：截至 2026 年 11 月，Fable 5.5 尚未被 Anthropic 官方发布。以下均为早期访问/路由报告。

所有测试均为「一句提示词 → 完整短片」，用户未手动修改代码或 Blender 场景。模型自主完成建模、绑定、动画、音乐、音效与自修 bug。

机器可读的索引数据见 [posts.json](posts.json)。

## 总览表

| Part | 标题 | 耗时 | 成本 | 时长 | 原帖 |
|------|------|------|------|------|------|
| 初始 | Clockwork Bird（发条鸟） | 1h54m | ~$20 | 60s | [链接](https://x.com/camperaigg/status/2117666378174050352) |
| Part 2 | Master Sword | 32min+ | $11.66 | - | [链接](https://x.com/camperaigg/status/2117694354685092255) |
| Part 3 | Anime Stickman Fight | 66min | $15.71 | 46s | [链接](https://x.com/camperaigg/status/2117717189059026969) |
| Part 4 | Transformer Truck | 107min | $9.64 | 12.5s | [链接](https://x.com/camperaigg/status/2117914482752299311) |
| Part 5 | Howl's Moving Castle | 133min | $12.37 | 35s | [链接](https://x.com/camperaigg/status/2117966825048997914) |
| Part 6 | Mechanical Heart | 106min | $12.35 | 30s | [链接](https://x.com/camperaigg/status/2118002649929056373) |
| Part 7 | Whale Breach | 154min | $17.85 | 31s | [链接](https://x.com/camperaigg/status/2118069524306284556) |

## 详细记录

### 初始测试：Clockwork Bird
- **提示词**：一句（未公开完整原文）
- **工具**：Claude Code + HyperFrames
- **亮点**：全矢量发条鸟零件飞入组装、连续镜头、原创华尔兹贯穿全片、纯数学合成音效（点击与帧精确同步 ±5ms）

### Part 2：Link's Master Sword
- **提示词**：Build Link's Master Sword in Blender（后续追加“make a video of it”）
- **亮点**：单脚本完整建模（Triforce 浮雕、编织握把、多层羽毛护手）、自动修复 z-fighting、连续运镜 + 森林光影 + 原创管弦乐

### Part 3：Anime Stickman Sword Fight
- **提示词**：Make me a video of 2 stickman fighting, anime style.
- **亮点**：骨骼 + 120Hz 布料、闪电刀 vs 火焰大剑、一帧冲击闪（mono/inverted/duotone）、16 乐器 120BPM 原创配乐、228 个物理同步音效（其中 79 个自动从剑尖速度检测）、高潮前全静音

### Part 4：Transformer Truck
- **提示词**：Make me a transformer truck with animations of its transforming.
- **亮点**：51 关节完整绑定 + 地面求解、Geometry Nodes 雨滴与涟漪、64 个纯合成音效（柴油/气刹/舵机等）

### Part 5：Howl's Moving Castle
- **提示词**：Make me Howl's moving castle and also show its internal machinery.
- **亮点**：完整蒸汽机→齿轮系→四足行走（从着地脚反解）、中途开壳剖视、步频精确华尔兹（1.4s/拍）、自动发现并优化草渲染（9.3s→4.2s/帧）

### Part 6：Mechanical Heart
- **提示词**：Make a mechanical heart and show its insides, use blender.
- **亮点**：双活塞曲轴、开壳动画、黄金油液气泡与滴落、心跳同步配乐、自动排查隐藏灯光问题

### Part 7：Whale Breach
- **提示词**：Make a whale breach a cel-shaded ocean.
- **亮点**：1690 万粒子流体（1200 steps/s）、三层 FFT 波浪 + cel-shading、109 万三角纯代码鲸鱼、水下光学（Snell's window）、自动发现并重渲染交叉线问题

## 说明与版权
- 所有视频与描述均来自原作者 @camperaigg 的公开推文，请以原帖为准。
- 本仓库仅做整理与索引，不托管视频文件。
- 如原作者后续公开代码/完整提示词，欢迎提交 PR 补充。

## 相关资源
- 其他 Fable 5.5 社区合集：[awesome-fable5-5-videos](https://github.com/billyhetech/awesome-fable5-5-videos)、[awesome-fable-5.5-usecase](https://github.com/coolbat/awesome-fable-5.5-usecase)

## License
本仓库的整理与索引部分以 [MIT License](LICENSE) 发布；索引所指向的原帖内容与视频版权归原作者 @camperaigg 所有。
