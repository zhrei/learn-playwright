"""
Test the API example

Author: Reidolvo (reidolvo@gdplabs.id)
"""

from typing import Any, Dict, Final

import pytest
from playwright.async_api import APIRequestContext, Playwright, async_playwright

BASE_URL: Final[str] = "https://jsonplaceholder.typicode.com"
RESOURCE_PATH: Final[str] = "/todos/1"

async def start_playwright() -> Playwright:
    """Starts the playwright instance
    
    Returns:
        Playwright: The playwright instance
    """
    return await async_playwright().start()


async def new_api_context(playwright: Playwright) -> APIRequestContext:
    """Creates a new API request context
    
    Args:
        playwright: The playwright instance
    
    Returns:
        APIRequestContext: The API request context
    """
    return await playwright.request.new_context(base_url=BASE_URL)


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
async def test_api_get_todo_by_id_returns_expected_fields() -> None:
    """Tests that the API returns the expected fields"""
    playwright = await start_playwright()
    ctx = await new_api_context(playwright)
    data = await get_json(ctx, RESOURCE_PATH)
    await stop_playwright(playwright, ctx)

    assert data.get("id") == 1
    assert isinstance(data.get("title"), str)
    assert {"userId", "completed"}.issubset(data.keys()) 