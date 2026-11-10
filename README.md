# 中文课题申报助手

一个面向中国课题申报的 AI Agent Skill。根据当次申报指南、已有申请资料和最新修改稿，协助完成方向判断、申报论证、申请人基础整理、工作计划、文献核查与语言润色。

重点适用于教育教学改革与社会科学类课题，也可按具体指南用于其他申报。它不附带固定申报模板，不预设申请人、项目类别、研究周期或成果数量。

## 能做什么

- **读懂指南**：区分重点、一般等类别的申报条件与结项要求，说明选题主要对应哪个方向。
- **补强论证**：把实际问题、研究内容、目标、方法和预期成果对应起来，避免用研究方法代替研究目标。
- **整理前期基础**：从真实课程、案例、教材、论文和项目中找到与本次任务有关的依据。
- **形成具体计划**：写清时间、任务和阶段成果；教改项目需要时补充课程安排。
- **核查文献**：默认采用 APA 作者—年份格式；指南另有要求时按当次规范处理。
- **尊重修改稿**：以用户指定的最新稿为准，使用自然、直接的中文，完整修订默认另存新版本。

只问方向、参考文献或一句话的用语时，技能只处理指定部分。只要求 prompt 或待审方案时，不提前执行后续写作。

## 安装

仓库名称为 `chinese-grant-assistant`，技能调用名称保持为 `cn-grant-application`。

在 Codex 中，将本仓库的 [`skills/cn-grant-application`](skills/cn-grant-application) 文件夹复制到个人技能目录 `~/.codex/skills/`。如果已有同名技能，先保留旧版本，再按需要更新。

也可以把下面这句话交给支持技能安装的助手：

```text
请安装这个 GitHub 仓库中的技能：
https://github.com/RayonLee/chinese-grant-assistant/tree/main/skills/cn-grant-application
```

其他支持 `SKILL.md` 的工具可按各自的技能安装约定使用。Word、PDF 读取与排版检查，以及联网检索，取决于使用环境提供的工具。

## 使用示例

### 新课题申报

```text
使用 $cn-grant-application，阅读这次申报指南和我提供的已有材料，
判断适合的方向，按申报表完成一版申请书。
引用要真实，文内作者—年份，文后统一参考文献。
工作计划要有具体时间和阶段成果，缺少的真实信息单独列出。
```

### 在修改稿上继续完善

```text
使用 $cn-grant-application，以我最新修改的申请书为基础，
只修改研究目标、要解决的问题和工作计划。
保留其他内容，使用自然的中文，遵守各栏字数限制。
```

### 只判断方向

```text
使用 $cn-grant-application，按本次指南判断我的选题对应哪个方向，
说明依据，并区分申报条件和结项要求，不重写申请书。
```

### 只生成待审 prompt

```text
使用 $cn-grant-application，先阅读指南和已有材料，
整理成一份可执行的写作 prompt，保存为本地 txt。
等我检查后再执行申报书写作。
```

## 字数自检

技能附带 `scripts/check_sections.py`，只需要 Python 3 和标准库。输入示例：

```json
{
  "sections": [
    {
      "name": "研究内容",
      "limit": 500,
      "texts": ["正文、引文和表格中的所有文字"]
    }
  ]
}
```

运行：

```bash
python3 skills/cn-grant-application/scripts/check_sections.py sections.json
```

工具按 Unicode 非空白字符计数，包含标点、引文和传入的表格文字，每个英文字母单独计数。这是保守自检口径，不等同于 Word 或资助方的字数统计。退出码：`0` 未超限，`1` 超限，`2` 输入有误。

## 文件结构

```text
skills/cn-grant-application/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── intake-and-plan.md
│   ├── evidence-and-writing.md
│   ├── review-and-delivery.md
│   └── sources-and-adaptation.md
└── scripts/check_sections.py
```

## 来源与使用边界

本技能重新编写了适合中国课题申报的流程，借鉴 ChineseResearchLaTeX 的三项申报写作技能，以及 K-Dense 的 `research-grants`、`citation-management`。具体版本、方法和适配方式见[来源与适配说明](skills/cn-grant-application/references/sources-and-adaptation.md)。不需要同时安装这些上游技能，本仓库未打包其源码和模板。

技能不编造履历、数据、合作承诺或引用，不保证立项。申报事实、指南合规性和最终提交由申报人确认；使用技能不代表授权助手提交申请、发送邮件或代为签署。

## 许可证

本项目新增内容采用 [MIT License](LICENSE)。方法来源与适配说明保留在上述来源文档中；本项目的 MIT 授权不改变上游项目的版权和许可。
