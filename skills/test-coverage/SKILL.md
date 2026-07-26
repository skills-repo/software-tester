---
name: test-coverage
description: 测试覆盖率分析，识别未覆盖分支并自动生成补充用例
source:
  type: original
  repo: skills-repo/software-tester
  path: skills/test-coverage/SKILL.md
  version: 1.0.0
  updated: 2026-07-26
metadata:
  category: 覆盖率
  platform: 通用
  difficulty: 入门
---

# 测试覆盖率分析

> 分析测试覆盖率报告，识别测试盲区，自动生成补充测试用例。

## 能力

- **覆盖率解析**：读取 Istanbul/Jacoco/coverage.py 等覆盖率报告
- **盲区识别**：定位未覆盖的分支、函数、行
- **优先级排序**：按风险等级排序未覆盖代码（核心逻辑 > 工具函数 > 配置）
- **用例补全**：为高风险盲区自动生成测试用例
- **阈值检查**：验证覆盖率是否达到项目配置的目标

## 使用方式

在 Claude Code 中使用 `/test-coverage` 调用。

```
/test-coverage 分析当前项目的测试覆盖率
/test-coverage 让覆盖率提升到 80%
```

## 工作流

1. 运行项目的测试覆盖率命令
2. AI 解析覆盖率报告
3. 按风险等级列出未覆盖的代码
4. 为高风险代码生成测试用例
5. 输出补充测试后的预期覆盖率

## 适用场景

- CI 中覆盖率不达标时的快速补充
- 新项目建立测试基准
- 重构前的覆盖率审计
- PR 审查时检查新增代码的测试覆盖

## 限制

- 不处理端到端/集成测试的覆盖率
- 覆盖率 100% 不意味着无 bug，仅识别未测试路径
- 需要项目已配置覆盖率工具