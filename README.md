# Paper to Presentation

给 Codex 一篇研究论文的 PDF，生成一份最多 8 页的可编辑 PowerPoint 和一份与它逐页对应的同语言口播稿。适用于方法、算法、实证研究、数据集、综述、系统和领域案例等论文。论文 PDF 是唯一必需输入。

## 使用方法

在 Codex 中打开本项目并附上论文 PDF。可以在请求里指定「中文」或「英文」，所选语言同时用于 PPT 和口播。省略语言时，默认交付全英文。

> 请读取 `paper-to-presentation/SKILL.md`，把附件里的论文做成一份中文讲解 PPT 和一份中文口播稿。

需要面向特定听众时，可补充受众、希望讲多久或重点讲哪部分。默认假定听众具备相关学术背景但尚未读过论文，口播目标为约 6–10 分钟，上限为 15 分钟。

| 选择 | PPT | 逐页口播稿 |
| --- | --- | --- |
| 英文（默认） | `presentation.pptx`，英文 | `narration.en.md` |
| 中文 | `presentation.pptx`，中文 | `narration.zh-CN.md` |

每次交付一份 16:9 可编辑 PPT 和一份口播稿。PPT 含封面或总结在内最多 8 页，口播稿逐页标注预计用时。

## Skill 文件

- [SKILL.md](paper-to-presentation/SKILL.md) 定义生成流程、语言选择和交付要求。
- [slides.md](paper-to-presentation/references/slides.md) 规定如何组织论文证据、处理原图并检查 PPT。
- [narration.md](paper-to-presentation/references/narration.md) 规定逐页口播的内容、格式与估时方法。

## 可选的交付检查

[check_delivery.py](paper-to-presentation/scripts/check_delivery.py) 读取已经生成的 PPTX 和 Markdown 口播稿，核对页数、16:9 比例、隐藏页、逐页口播顺序和时长标注。它也会检查每页有正文，且各页标注时长之和等于总时长，最多 15 分钟。在项目根目录用 Python 3 运行对应命令。

```powershell
# 英文（默认）
python paper-to-presentation/scripts/check_delivery.py presentation.pptx narration.en.md
# 中文
python paper-to-presentation/scripts/check_delivery.py --language zh-CN presentation.pptx narration.zh-CN.md
```

传入两个成品的实际路径。`--language` 选择口播稿的标题和时长标注格式。事实准确性、正文语言、PPT 视觉效果和实读时长由生成流程另外复核。
