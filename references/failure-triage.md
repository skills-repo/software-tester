# 失败分诊（Failure Triage）

> 拿到一堆红色测试后，**先分诊再下结论**。把「环境噪音」误报成产品缺陷，比漏报更伤信任——尤其是要对外提 issue 时。

## 何时使用

- 跑完测试套件出现大量失败，需要判断哪些是真 bug
- 准备把失败写成 issue / 缺陷报告之前（**必做**）
- 用户说「测试全红了」「这些失败是真的吗」

## 核心原则

**没有验证过根因的失败，不许写进 issue。** 每条要上报的失败都必须能回答：
1. 根因是什么（精确到文件:行）？
2. 换一台干净机器还会失败吗？
3. 是产品代码错了，还是测试自身错了？

## 分诊四象限

| 类别 | 特征 | 处理 |
|------|------|------|
| **真缺陷** | 纯逻辑/纯文本断言失败，与机器无关 | 上报 |
| **环境噪音** | 原生模块、权限、沙箱、路径 | **不上报**，报告中单列 |
| **负载抖动** | 超时类，隔离重跑即过 | 不上报，标记 flaky 观察 |
| **测试自身缺陷** | 产品对，mock/断言写错 | 上报，但标 `testing` 而非产品 bug |

## 环境噪音识别清单

命中以下任一，几乎可以断定不是项目缺陷：

- **原生模块 ABI 不匹配**：`NODE_MODULE_VERSION 147 ... requires 127`
  → 本机 node_modules 用另一版本 Node 编译的。`npm rebuild` 即可。
- **沙箱/权限拦截**：报错栈里出现 IDE、Agent 宿主或 shim 的路径
  （如 `/Applications/*.app/.../safe-delete.cjs`、`EACCES ... mkdir /var/folders/...`）
  → 是宿主工具在拦 `fs.rmSync`，与被测项目无关。
- **可执行文件缺失**：`python3 not found`、`docker daemon not running`
- **临时目录/HOME 被重定向**

判断口诀：**报错栈里出现被测仓库以外的路径 → 优先怀疑环境。**

## 负载抖动 vs 确定性失败

并发跑覆盖率 + 多 worker 时，PTY / 子进程 / 超时类测试极易假失败。

```bash
# 隔离重跑：单文件 + 串行 + 无其他负载
npx jest tests/<file>.test.ts --runInBand
```

- 隔离后**通过** → 负载抖动，不上报（可建议加超时或标记）
- 隔离后**仍失败** → 确定性失败，继续挖根因

> 症状对照：`SIGTERM` / `status:null` 多为被外部杀掉（负载）；
> `Exceeded timeout of Xms` 且隔离仍复现，则是真的挂住了。

## 并发修改陷阱（重要）

如果仓库同时被别的进程/agent 编辑，会出现「幽灵编译错误」：

```
error TS2304: Cannot find name 'debugError'
```
但几分钟前 `tsc --noEmit` 明明是干净的。

排查：
```bash
find src -name "*.ts" -newermt "-15 minutes" -exec ls -la {} \;   # 谁刚被改
git status --short <file>                                          # 是否未提交改动
npx tsc --noEmit                                                   # 现在还错吗
```
若文件 mtime 落在你的会话区间内 → 是**中途编辑竞态**，不是缺陷，重跑即可。

同理，上报前务必确认失败文件**没有本地未提交改动**：
```bash
git status --short src/<path> tests/<path>   # 应为空，否则失败可能来自本地脏状态
```

## 脏工作区是双向的：既造假阳，也**掩盖真缺陷**

上一条只防「脏改动制造假失败」。反方向同样成立且更危险：
**未提交的 WIP 可能正好修好了 HEAD 上的 bug，让你在本地看到全绿，而用户拿到的 HEAD 是坏的。**

所以只要 `git status` 非空，**必须在干净检出上再跑一遍基线**：

```bash
git worktree add --detach /tmp/<proj>-clean HEAD
ln -s "$PWD/node_modules" /tmp/<proj>-clean/node_modules   # 避免重装依赖
cd /tmp/<proj>-clean && npx jest --runInBand --silent 2>&1 | grep -E "^FAIL|^Tests:"
```

**差分分诊表**（对比「脏工作区」与「干净 HEAD」两次结果）：

| 脏 | 干净 | 结论 |
|----|------|------|
| FAIL | PASS | 本地 WIP 造成，**不上报** |
| PASS | **FAIL** | **HEAD 真缺陷、被本地 WIP 掩盖 —— 最高价值，优先上报** |
| FAIL | FAIL | 真失败，继续挖根因 |
| 两次不一致 | | flaky，隔离重跑再判 |

配套查提交史，往往能还原回归故事：
```bash
git log --oneline -3 -- <impl-file> <test-file>
git merge-base --is-ancestor <test-commit> <impl-commit> && echo "先加测试，后改实现"
```
典型模式：**某次提交移除/改动了实现却没同步删改测试 → HEAD 带着红测试发布。**

注意：干净 worktree 没有 `dist/`，依赖编译产物的测试会整片假失败——先 `npm run build` 或直接排除。

> 清理：`git worktree remove <path> --force`；被宿主安全策略拦截时用 `mv` 挪走再 `git worktree prune`。

## 定位根因：让证据说话

不要靠读代码猜。**插桩打印真实运行时事实。**

```bash
npx jest tests/x.test.ts --runInBand   # 先确认可复现
```

插桩要点：
- 若测试 mock 了 `process.stdout.write`，`console.log` 会被吞掉
  → 改用 `require('fs').appendFileSync('/tmp/probe.log', msg)`
- 给 hang 住的 promise 加 `Promise.race` + 超时哨兵，区分「未 resolve」与「抛错」
- 记录**调用次数与顺序**，单槽位回调（`x = () => cb()`）被后续调用覆盖是经典 hang 根因

## 上报前自检

- [ ] 隔离重跑复现过
- [ ] 根因精确到 文件:行
- [ ] 排除了环境噪音与本地脏改动
- [ ] 复现步骤是可直接粘贴执行的最小片段
- [ ] 贴的是**实际输出**，不是想象的输出
- [ ] 搜过现有 issue，不重复（`gh issue list --state all`）
- [ ] 区分「产品缺陷」与「测试缺陷」，打对标签

## 清理

自己为取证创建的临时测试/脚本，**必须删干净**再结束：

```bash
git status --short tests/    # 确认没留下 probe/poc 文件
```
若 `rm` 被宿主安全策略拦截，用 `mv` 移出仓库。

## 限制

- 分诊给的是判据，不替你拍板严重级别。
- 「环境噪音」结论只对当前机器成立；若 CI 上同样失败，需重新归类。
