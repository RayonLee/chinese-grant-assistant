# 来源与适配说明

本技能依据实际课题申报修订及试用反馈整理。它是面向中国教改、社科等申报工作的独立流程，不要求同时安装以下五个上游技能。

| 试用来源 | 本技能保留的方法 | 适配方式 |
| --- | --- | --- |
| ChineseResearchLaTeX / nsfc-justification-writer（试用v1.9.0） | 问题、已有证据、待解决问题之间的联系 | 按本次资助方栏目和字数写，不强制国自然结构 |
| 同仓库 / nsfc-research-foundation-writer（v0.1.2） | 已有成果与本次任务对应，区别事实和计划 | 适用于课程、案例、教材、研究及真实资源，不固定申请人 |
| 同仓库 / nsfc-research-content-writer（v1.0.0） | 研究任务、目标、成果、时间相互对应 | 使用本次周期，教改需要时增加课程安排 |
| K-Dense / citation-management（v2.3） | 题录核查、来源定位、引文与文后条目核对 | 默认APA，服从当次要求；独立核对论点，不依赖脚本成功状态 |
| K-Dense / research-grants（v1.5） | 从申报要求逐项检查文本 | 用作检查方法，不套国外基金模板 |

上游地址：

- https://github.com/huangwb8/ChineseResearchLaTeX
- https://github.com/K-Dense-AI/scientific-agent-skills

本技能重新编写流程和示例，没有打包上游源码、LaTeX模板或固定学术参考文献库。保留的写作原则包括自然中文、真实作者年份引文、尊重最新修改稿、具体时间表和深挖真实申请人基础。原项目的周期、团队、模型和成果数量不作为通用默认值。

K-Dense工具来源论文（仅用于工具溯源，不自动写进新课题的学术参考文献）：

Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific agent skills: A library of procedural knowledge for research agents*. arXiv. https://doi.org/10.48550/arXiv.2609.00065

本技能格式和调用方式参考OpenAI官方技能文档：
https://learn.chatgpt.com/docs/build-skills

以后维护应以实际使用中出现的问题为依据，进行必要的小幅修订。不能因一次课题的特殊情况，为所有未来课题增加固定流程或限制。
