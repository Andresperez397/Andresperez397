"""Visit the portfolio's Streamlit apps so they don't go to sleep, and wake any that have.

Streamlit Community Cloud puts an app to sleep after a stretch with no visitors; a sleeping app shows a
"wake up" button instead of the app. Opening each app in a real browser counts as a visit, and if an app
is already asleep this clicks the button and waits until the app has rendered.
"""

from __future__ import annotations

import re
import sys

from playwright.sync_api import sync_playwright

APPS = [
    "https://pitch-types-are-relative.streamlit.app/",
    "https://retail-operations-dashboard.streamlit.app/",
    "https://elbow-torque-explorer.streamlit.app/",
]
WAKE_BUTTON = re.compile("get this app back up", re.I)


def app_rendered(page) -> bool:
    return any(f.locator('[data-testid="stAppViewContainer"]').count() for f in page.frames)


def visit(page, url: str) -> str:
    page.goto(url, wait_until="domcontentloaded", timeout=90_000)
    page.wait_for_timeout(8_000)
    woke = False
    button = page.get_by_role("button", name=WAKE_BUTTON)
    if button.count():
        button.first.click()
        woke = True
    for _ in range(60):  # up to 5 minutes for a cold start
        if app_rendered(page):
            page.wait_for_timeout(5_000)  # hold the session briefly so it registers as a visit
            return "woken" if woke else "awake"
        page.wait_for_timeout(5_000)
    return "did not load"


def main() -> int:
    failed = False
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for url in APPS:
            page = browser.new_page()
            status = visit(page, url)
            print(f"{status:12} {url}")
            failed |= status == "did not load"
            page.close()
        browser.close()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
