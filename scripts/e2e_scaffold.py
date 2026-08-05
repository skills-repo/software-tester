#!/usr/bin/env python3
"""Scaffold a Playwright E2E test from a list of steps.

Usage:
    python3 scripts/e2e_scaffold.py --name 登录流程 \
        --steps "打开 /login;输入账号 hope;输入密码 secret;点击提交;断言跳转 /dashboard"
    python3 scripts/e2e_scaffold.py --name 登录流程 --steps "..." --output tests/login.spec.ts
"""
import argparse
import re
import sys

STEP_RE = re.compile(
    r"^(?:打开|导航到|访问)\s*(\S+)"              # 打开 /login
    r"|^(?:输入|填写|键入)\s*(\S+)\s+(.+)"          # 输入 账号 hope（允许无空格）
    r"|^(?:点击|按下)\s*(.+)"                        # 点击 提交
    r"|^(?:断言跳转|跳转断言|断言)\s*(\S+)"          # 断言跳转 /dashboard
)


def render_step(step):
    s = step.strip()
    if not s:
        return None
    m = STEP_RE.match(s)
    if m:
        open_url, field, value, click, assert_url = m.groups()
        if open_url:
            return f"  await page.goto('{open_url}');"
        if field and value:
            sel = field
            return (f"  await page.getByLabel('{field}').fill('{value}');"
                    if not field.startswith("/") else
                    f"  await page.locator('{sel}').fill('{value}');")
        if click:
            return f"  await page.getByRole('button', {{ name: '{click}' }}).click();"
        if assert_url:
            return f"  await expect(page).toHaveURL('{assert_url}');"
    # fallback: comment
    return f"  // TODO: {s}"


def main():
    ap = argparse.ArgumentParser(description="Scaffold a Playwright E2E test.")
    ap.add_argument("--name", required=True, help="test / flow name")
    ap.add_argument("--steps", required=True, help="semicolon-separated steps")
    ap.add_argument("--output", help="write to file instead of stdout")
    args = ap.parse_args()

    steps = [render_step(s) for s in args.steps.split(";")]
    steps = [s for s in steps if s]
    body = "\n".join(steps)

    code = f"""import {{ test, expect }} from '@playwright/test';

test('{args.name}', async ({{ page }}) => {{
{body}
}});
"""
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(code)
        print(f"written: {args.output}", file=sys.stderr)
    else:
        print(code)


if __name__ == "__main__":
    main()
