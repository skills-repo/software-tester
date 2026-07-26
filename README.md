# 软件测试技能库

> AI Agent Skills for Software Testing —— 覆盖单元测试、E2E 测试、API 测试、覆盖率分析

## 定位

为软件开发者提供一套可安装的 AI Agent 测试技能，让 Claude Code 等 AI 编程助手成为你的自动化测试搭档。

## 核心理念

> 写好测试是工程纪律，不是负担。用 AI 降低测试编写成本，让每一个 PR 都有测试护航。

- **测试先行**——先写测试再写代码，AI 帮你生成测试骨架
- **聚焦质量**——不仅测功能正确性，还测边界、异常、性能退化
- **可落地执行**——每个技能输出可直接运行的测试代码

## 技能清单

| 环节 | 技能 | 描述 |
|------|------|------|
| 🧪 E2E | `e2e-testing` | Playwright/Cypress 端到端测试生成与维护 |
| 🔬 单元测试 | `unit-test-writer` | 自动生成单元测试，Jest/Vitest/Pytest |
| 🔗 API 测试 | `api-testing` | REST/GraphQL API 测试用例生成 |
| 📊 覆盖率 | `test-coverage` | 测试覆盖率分析与缺失用例补充 |

## 快速开始

```bash
# 安装全部技能
npx skills add skills-repo/software-tester@e2e-testing -g -y
npx skills add skills-repo/software-tester@unit-test-writer -g -y
npx skills add skills-repo/software-tester@api-testing -g -y
npx skills add skills-repo/software-tester@test-coverage -g -y
```

## 推荐工作流

```
单元测试 → API 测试 → E2E 测试 → 覆盖率检查
unit-      api-        e2e-       test-
test       testing     testing    coverage
writer
```

## 许可

MIT