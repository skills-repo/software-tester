# software-tester（超级技能 · Superpowers 架构）

> 一个完整的软件测试技能：让 AI 编程助手成为覆盖测试金字塔全层的专业测试工程搭档。

采用 **Superpowers 架构**：薄 `SKILL.md` 作路由，`references/` 存放按需加载的完整 playbook，`scripts/` 提供确定性可重复脚本，`assets/` 提供即取即用的配置与模板。上下文按需渐进式加载（progressive disclosure）。

## 覆盖能力

| 域 | Playbook | 关键工具 |
|----|----------|----------|
| 单元测试 / 覆盖率 | `references/unit-testing.md` | pytest / Jest / Vitest |
| 端到端 | `references/e2e-testing.md` | Playwright Test |
| API 测试 | `references/api-testing.md` | REST / GraphQL |
| 测试策略 / 治理 | `references/test-strategy.md` | 金字塔 / CI 门禁 |
| TDD | `references/tdd.md` | red-green-refactor |
| 性能 / 压测 | `references/performance-testing.md` | k6 / Locust |
| 安全测试 | `references/security-testing.md` | OWASP API Top 10 |
| 可视化回归 | `references/visual-regression.md` | Playwright / Percy |
| 契约测试 | `references/contract-testing.md` | Pact (CDC) |
| 报告 / 风险 | `references/reporting.md` | 计划 / 矩阵 / 风险 |

## 目录结构

```
software-tester/
├── SKILL.md                 # 薄路由：触发词 + 能力索引 + 脚本/资源索引 + 核心原则
├── README.md                # 本文件
├── AGENTS.md                # AI 助手使用指引
├── references/              # 10 个按需加载的 playbook
├── scripts/                 # 确定性脚本
│   ├── run_coverage.py      # 运行覆盖率并汇总未覆盖行
│   ├── gen_test_plan.py     # 生成测试计划
│   ├── test_matrix.py       # 生成 API 测试矩阵
│   └── e2e_scaffold.py      # 生成 Playwright 测试骨架
└── assets/                  # 模板与配置
    ├── ci-coverage.yml
    ├── test-plan-template.md
    ├── playwright.config.template.ts
    └── jest.config.template.js
```

## 快速开始

```bash
# 覆盖率
python3 scripts/run_coverage.py ./src --lang python
# 测试计划
python3 scripts/gen_test_plan.py --name 支付模块 --features 创建订单,退款
# API 测试矩阵
python3 scripts/test_matrix.py --method POST --path /api/login --params username,password --auth
# E2E 骨架
python3 scripts/e2e_scaffold.py --name 登录流程 --steps "打开 /login;输入账号 hope;点击提交"
```

## 设计原则

1. 测试先行（TDD 优先）
2. 测试金字塔（单测 70% / 集成 20% / E2E 10%）
3. 覆盖 ≠ 质量
4. 产出可运行、脚本确定
5. 先读对应 playbook 再动手
6. 专项结果以报告呈现，不替 QA 拍板策略

## 许可

MIT
