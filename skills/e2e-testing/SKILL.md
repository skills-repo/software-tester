---
name: e2e-testing
description: Playwright/Cypress 端到端测试生成与维护，自动识别页面交互流程生成测试用例
metadata:
  category: E2E测试
  platform: Web
  difficulty: 进阶
---

# E2E 端到端测试

> 自动识别用户流程，生成可维护的 Playwright/Cypress 端到端测试。

## 能力

- **页面交互识别**：分析组件代码，自动提取用户操作流程
- **测试用例生成**：基于交互流程生成 Playwright/Cypress 测试代码
- **选择器优化**：优先使用 `data-testid`，自动建议语义化选择器
- **失败诊断**：分析测试失败截图和日志，定位根因
- **CI 集成**：输出可直接用于 GitHub Actions 的测试配置

## 使用方式

在 Claude Code 中使用 `/e2e-testing` 调用。

```
/e2e-testing 为登录页面生成 E2E 测试
/e2e-testing 分析上一次测试失败的原因
```

## 工作流

1. 指定要测试的页面或用户流程
2. AI 分析组件结构，提取交互路径
3. 生成测试用例（正常路径 + 异常路径 + 边界情况）
4. 输出 Playwright/Cypress 测试代码
5. 提供运行命令和 CI 配置建议

## 适用场景

- 新功能上线前的 E2E 测试编写
- 回归测试用例补充
- 关键业务流程（登录、支付、下单）测试覆盖
- 跨浏览器兼容性测试

## 限制

- 不处理原生移动应用测试（需配合 Appium 等工具）
- 不生成性能/压力测试用例
- 复杂动画/Canvas 交互需人工补充验证逻辑