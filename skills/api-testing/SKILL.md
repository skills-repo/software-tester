---
name: api-testing
description: REST/GraphQL API 测试用例生成，覆盖状态码、参数校验、鉴权和响应结构
source:
  type: original
  repo: skills-repo/software-tester
  path: skills/api-testing/SKILL.md
  version: 1.0.0
  updated: 2026-07-26
metadata:
  category: API测试
  platform: API
  difficulty: 进阶
---

# API 测试

> 为 REST 和 GraphQL API 生成全面的测试用例和自动化测试脚本。

## 能力

- **接口分析**：从 OpenAPI/Swagger/GraphQL schema 自动提取测试点
- **用例生成**：覆盖 2xx/4xx/5xx 状态码、必填/可选参数、鉴权
- **契约测试**：验证响应结构与 schema 定义一致
- **集成测试**：多接口串联的业务流程测试
- **脚本输出**：SuperTest、Jest、Pytest、k6 等多种格式

## 使用方式

在 Claude Code 中使用 `/api-testing` 调用。

```
/api-testing 根据这个 OpenAPI 文档生成测试用例
/api-testing 为 /users 接口生成完整的测试套件
```

## 工作流

1. 提供 API 定义（OpenAPI 文件、GraphQL schema 或接口代码）
2. AI 分析接口参数、响应结构、鉴权方式
3. 生成测试用例清单（正向 + 异常 + 边界）
4. 生成自动化测试代码
5. 输出环境配置和运行说明

## 适用场景

- 新 API 上线前的测试编写
- 前后端分离项目的契约测试
- API 版本升级时的回归测试
- 第三方 API 集成的 mock 测试

## 限制

- 不处理 WebSocket/gRPC 测试（未来扩展）
- 性能/压力测试需配合 k6 等专用工具
- 需要 API 文档或代码作为输入