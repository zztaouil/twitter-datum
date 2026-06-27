#!/usr/bin/env python3
"""
Requirements:
  pip install nodriver pyotp

Usage:
  python3 tools/create_sessions_browser.py <accounts_file> [--append sessions.jsonl] [--headless] [--delay N]

Input (accounts_file):
  [{"username": "user", "password": "pass", "totp": "totp_seed_or_empty_string"}, ...]

Output:
  {"kind": "cookie", "username": "...", "id": "...", "auth_token": "...", "ct0": "..."}
"""

import asyncio
import json
import sys
from time import sleep

import nodriver as uc
import pyotp


async def login_and_get_cookies(account, headless=False):
    browser = await uc.start(headless=headless)
    tab = await browser.get("https://x.com/i/flow/login")

    username = account["username"]
    password = account["password"]
    totp_seed = account.get("totp", "")

    try:
        print(f"[*] Entering username {username}...", file=sys.stderr)

        retry = 0
        while retry < 5:
            username_input = await tab.find('input[autocomplete="username"]', timeout=10)
            pos = await username_input.get_position()
            await tab.mouse_move(pos.x, pos.y, steps=50, flash=True)
            await asyncio.sleep(0.1)
            await username_input.click()
            await asyncio.sleep(0.5)
            await username_input.send_keys(username)
            await asyncio.sleep(0.2)
            await username_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                retry += 1
                wait = retry * 10
                print(f"Retrying in {wait} seconds...", file=sys.stderr)
                await asyncio.sleep(wait)
            else:
                break

        print("[*] Entering password...", file=sys.stderr)
        pretry = 0
        while pretry < 5:
            password_input = await tab.find('input[autocomplete="current-password"]', timeout=15)
            await password_input.click()
            await asyncio.sleep(0.5)
            await password_input.send_keys(password)
            await asyncio.sleep(0.2)
            await password_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                pretry += 1
                wait = pretry * 10
                print(f"Retrying in {wait} seconds...", file=sys.stderr)
                await asyncio.sleep(wait)
            else:
                break

        page_content = await tab.get_content()
        if "verification code" in page_content or "Enter code" in page_content:
            if not totp_seed:
                raise Exception("2FA required but no TOTP seed provided")
            print("[*] 2FA detected, entering code...", file=sys.stderr)
            totp_code = pyotp.TOTP(totp_seed).now()
            code_input = await tab.select('input[type="text"]')
            await code_input.send_keys(totp_code + "\n")
            await asyncio.sleep(3)

        print("[*] Retrieving cookies...", file=sys.stderr)
        for _ in range(20):
            cookies = await browser.cookies.get_all()
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}

            if "auth_token" in cookies_dict and "ct0" in cookies_dict:
                user_id = None
                if "twid" in cookies_dict:
                    twid = cookies_dict["twid"]
                    if "u%3D" in twid:
                        user_id = twid.split("u%3D")[1].split("&")[0].strip('"')
                    elif "u=" in twid:
                        user_id = twid.split("u=")[1].split("&")[0].strip('"')

                cookies_dict["username"] = username
                if user_id:
                    cookies_dict["id"] = user_id

                return cookies_dict

            await asyncio.sleep(1)

        raise Exception("Timeout waiting for cookies")

    finally:
        browser.stop()


async def main():
    if len(sys.argv) < 2:
        print("Usage: python3 create_sessions_browser.py <accounts_file> [--append sessions.jsonl] [--headless] [--delay N]", file=sys.stderr)
        sys.exit(1)

    accounts_file = sys.argv[1]
    append_file = None
    headless = False
    delay = 1

    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--append":
            append_file = sys.argv[i + 1]
            i += 2
        elif arg == "--headless":
            headless = True
            i += 1
        elif arg == "--delay":
            delay = int(sys.argv[i + 1])
            i += 2
        else:
            print(f"[!] Warning: Unknown argument: {arg}", file=sys.stderr)
            i += 1

    with open(accounts_file) as f:
        accounts = json.load(f)

    if not accounts:
        print("No accounts in file", file=sys.stderr)
        sys.exit(0)

    for idx, acc in enumerate(accounts, 1):
        try:
            cookies = await login_and_get_cookies(acc, headless)
            session = {
                "kind": "cookie",
                "username": cookies["username"],
                "id": cookies.get("id"),
                "auth_token": cookies["auth_token"],
                "ct0": cookies["ct0"],
            }

            output = json.dumps(session)
            if append_file:
                with open(append_file, "a") as f:
                    f.write(output + "\n")
                print(f"✓ Session appended for {acc['username']}", file=sys.stderr)
            else:
                print(output)

            print(f"Progress: {idx} / {len(accounts)}", file=sys.stderr)
            if idx < len(accounts):
                sleep(delay)
        except Exception as error:
            print(f"[!] Error for {acc['username']}, skipping: {error}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
