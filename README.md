# Paper to Presentation

一个可直接装入 Codex 的 Skill。附上一篇研究论文 PDF，即可生成最多 8 页的可编辑 PowerPoint 和一份逐页对应的口播稿。适用于算法、实验研究、数据集、综述、系统和领域案例等论文。

## 安装

在 Codex 中发送下面这条请求。内置安装器会从 GitHub 安装该 Skill。

```text
$skill-installer 请安装 https://github.com/Fryderyk-Fan/paper-to-presentation/tree/main/paper-to-presentation
```

## 使用

安装后，在 Codex 中附上论文 PDF，然后调用 Skill。

```text
$paper-to-presentation 请把附件里的论文做成中文讲解 PPT 和口播稿。
```

默认交付**英文 PPT 和英文口播稿**。指定中文时，两份文件一起切换为中文。也可以在请求里指定受众、希望讲多久，或需要重点讲解的部分。

- **`presentation.pptx`** — 16:9 可编辑 PowerPoint，包含封面和总结在内最多 8 页。
- **`narration.en.md` 或 `narration.zh-CN.md`** — 与 PPT 逐页对应的口播，逐页标注预计用时。默认约 6–10 分钟，最长 15 分钟。

[查看 Skill 定义](paper-to-presentation/SKILL.md)
