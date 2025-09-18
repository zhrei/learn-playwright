"""
Test the API authentication example

Author: Reidolvo (reidolvo@gdplabs.id)
"""

from typing import Any, Dict, Final

import pytest
from playwright.async_api import APIRequestContext, Playwright, async_playwright

import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL: Final[str] = "https://httpbin.org"
BEARER_PATH: Final[str] = "/bearer"

async def start_playwright() -> Playwright:
    """Starts the playwright instance
    
    Returns:
        Playwright: The playwright instance
    """
    return await async_playwright().start()


def token_from_env() -> str:
    """Gets the token from the environment variables
    
    Returns:
        str: The token
    """
    return os.getenv("API_BEARER_TOKEN", "test-token")


async def new_authed_context(playwright: Playwright, token: str) -> APIRequestContext:
    """Creates a new API request context with authentication
    
    Args:
        playwright: The playwright instance
        token: The token
    
    Returns:
        APIRequestContext: The API request context
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return await playwright.request.new_context(base_url=BASE_URL, extra_http_headers=headers)


async def get_json(ctx: APIRequestContext, path: str) -> Dict[str, Any]:
    """Gets the JSON data from the API
    
    Args:
        ctx: The API request context
        path: The path to the resource
    
    Returns:
        Dict[str, Any]: The JSON data
    """
    response = await ctx.get(path)
    assert response.ok, f"HTTP {response.status} for {path}"
    return await response.json()


async def stop_playwright(playwright: Playwright, ctx: APIRequestContext) -> None:
    """Stops the playwright instance
    
    Args:
        playwright: The playwright instance
        ctx: The API request context
    """
    await ctx.dispose()
    await playwright.stop()


@pytest.mark.asyncio
async def test_api_auth_bearer_header_roundtrips_token() -> None:
    """Tests that the API authentication header roundtrips the token"""
    playwright = await start_playwright()
    token = token_from_env()
    ctx = await new_authed_context(playwright, token)
    data = await get_json(ctx, BEARER_PATH)
    await stop_playwright(playwright, ctx)

    assert data.get("authenticated") is True