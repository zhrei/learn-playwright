"""
Test the title of the Google search page

Author: Reidolvo (reidolvo@gdplabs.id)
"""

from typing import Final

import pytest
from playwright.async_api import Browser, Page, Playwright, async_playwright

import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_URL: Final[str] = "https://www.google.com"
EXPECTED_IN_TITLE: Final[str] = "Google"

async def start_playwright() -> Playwright:
    """Starts the playwright instance
    
    Returns:
        Playwright: The playwright instance
    """
    return await async_playwright().start()

async def launch_browser(playwright: Playwright) -> Browser:
    """Launches the browser
    
    Args:
        playwright: The playwright instance
    
    Returns:
        Browser: The browser instance
    """
    headless = os.getenv("HEADLESS", "true").lower() in ("true", "1")
    slow_mo = os.getenv("SLOW_MO", None)
    if os.getenv("BROWSER") == "firefox": 
        return await playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
    elif os.getenv("BROWSER") == "webkit": 
        return await playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
    else: 
        return await playwright.chromium.launch(headless=headless, slow_mo=slow_mo)

async def open_page(browser: Browser) -> Page:
    """Opens a new page
    
    Args:
        browser: The browser instance
    
    Returns:
        Page: The page instance
    """
    return await browser.new_page()


async def fetch_title(page: Page, url: str) -> str:
    """Fetches the title of the page
    
    Args:
        page: The page instance
        url: The url of the page
    
    Returns:
        str: The title of the page
    """
    await page.goto(url)
    return await page.title()


async def stop_playwright(playwright: Playwright, browser: Browser) -> None:
    """Stops the playwright instance
    
    Args:
        playwright: The playwright instance
        browser: The browser instance
    """
    await browser.close()
    await playwright.stop()


@pytest.mark.asyncio
async def test_google_title_contains_expected_text() -> None:
    """Tests the title of the Google search page contains the expected text"""
    playwright = await start_playwright()
    browser = await launch_browser(playwright)
    page = await open_page(browser)
    title = await fetch_title(page, GOOGLE_URL)
    await stop_playwright(playwright, browser)
    assert EXPECTED_IN_TITLE in title 