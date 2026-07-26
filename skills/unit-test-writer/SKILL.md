---
name: unit-test-writer
description: 自动生成单元测试，支持 Jest/Vitest/Pytest，覆盖正常路径、边界值和异常情况
source:
  type: original
  repo: skills-repo/software-tester
  path: skills/unit-test-writer/SKILL.md
  version: 1.0.0
  updated: 2026-07-26
metadata:
  category: 单元测试
  platform: 通用
  difficulty: 入门
---

# 单元测试编写器

> 给定函数或模块代码，自动生成高质量的单元测试。

## 能力

- **多框架支持**：Jest、Vitest、Pytest、Go testing、JUnit
- **全面覆盖**：正常输入、边界值、空值、异常输入、错误路径
- **Mock 生成**：自动识别外部依赖，生成对应的 mock/stub
- **测试数据工厂**：为复杂对象生成测试数据构造器
- **快照测试**：对 UI 组件自动生成快照测试

## 使用方式

在 Claude Code 中使用 `/unit-test-writer` 调用。

```
/unit-test-writer 为这个函数生成单元测试
/unit-test-writer 补全这个模块缺失的测试用例
```

## 工作流

1. 提供目标函数或模块代码
2. AI 分析函数签名、分支逻辑、外部依赖
3. 生成测试用例矩阵（happy path + edge cases + error cases）
4. 生成 mock 和测试数据
5. 输出完整可运行的测试文件

## 适用场景

- 新函数/模块的测试编写
- 遗留代码补充测试覆盖
- PR 审查时发现缺少测试
- 重构前先补齐测试安全网

## 限制

- 不处理需要硬件/特殊环境的测试
- 复杂并发/竞态条件的测试需人工审查
- 测试质量依赖输入代码的可测试性