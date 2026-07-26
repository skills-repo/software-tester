# AGENTS.md

## 仓库性质

这是一个 **AI Agent 技能库**，不是软件项目。所有内容为 Markdown 格式的技能定义文件。

## 目录约定

```
software-tester/
├── README.md              # 项目介绍和使用指南
├── AGENTS.md              # AI 助手使用指引（本文件）
└── skills/                # 技能目录
    ├── <skill-name>/      # 单个技能目录
    │   └── SKILL.md       # 技能定义文件
    └── ...
```

## SKILL.md 格式

每个技能文件遵循以下结构：

```markdown
---
name: <skill-name>
description: <一句话描述，显示在技能列表中>
metadata:
  category: <单元测试|E2E测试|API测试|覆盖率>
  platform: <Web|API|通用>
  difficulty: <入门|进阶|专家>
---

# <技能名称>

> <一句话简介>

## 能力

- 能力点列表

## 使用方式

在 Claude Code 中使用 `/skill-name` 调用。

## 工作流

1. 步骤化的执行流程

## 适用场景

- 场景列表

## 限制

- 不擅长的领域
```

## 工作约定

- 所有技能内容使用中文编写
- 技能聚焦单一测试环节
- 每个技能需明确"能做什么"和"不能做什么"
- 输出的测试代码必须可直接运行
- 覆盖主流测试框架：Jest、Vitest、Playwright、Cypress、Pytest

## 技能添加流程

1. 在 `skills/` 下创建以技能名命名的目录
2. 编写 `SKILL.md`
3. 确保 `metadata` 字段完整
4. 更新 `README.md` 中的技能清单表

## 不做什么

- 不创建测试管理平台类技能（那是 SaaS 产品的事）
- 不创建面向单一公司内部工具的技能
- 不替代 QA 团队的测试策略制定