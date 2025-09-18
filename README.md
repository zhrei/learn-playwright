# Overview

![Playwright Logo](docs/images/playwright_logo.png)

This repository is dedicated to learning and exploring Playwright, a powerful end-to-end testing framework developed by Microsoft. Playwright enables developers to automate browser actions, making it easier to test web applications across multiple browsers such as Chromium, Firefox, and WebKit. Playwright is also a vital component to be learnt if we are to build BUA (browser-use agent) as it is one of the core components to allowing agent-browser interaction.

Learn Playwright:
[[Youtube]](https://www.youtube.com/playlist?list=PLhW3qG5bs-L9sJKoT1LC5grGT77sfW0Z8) | [[Documentation]](https://playwright.dev/python/docs/intro)

## Key Features
- **Cross-browser testing**: Supports Chromium, Firefox, and WebKit with a single API
- **Auto-wait functionality**: Automatically waits for elements to be ready before performing actions
- **Network interception**: Ability to mock and modify network requests and responses
- **Mobile device emulation**: Test on various mobile devices and screen sizes
- **Parallel test execution**: Run tests concurrently to reduce execution time
- **Built-in test runner**: Comes with its own test runner with rich reporting capabilities
- **Headless and headed modes**: Run tests with or without browser UI
- **Screenshot and video recording**: Capture visual evidence of test execution
- **Multiple language support**: Available for JavaScript, TypeScript, Python, Java, and .NET
- **Reliable element selection**: Advanced selectors including text, CSS, and XPath

## Prerequisites
1. Python 3.8 or higher
2. Supported OS:
    - Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL)
    - macOS 14 Ventura, or later
    - Debian 12, Debian 13, Ubuntu 22.04, Ubuntu 24.04, on x86-64 and arm64 architecture
3. UV dependency manager

## Setting Up
1. Clone this repository

2.  Activate `venv` and install dependencies
    ```bash
    uv venv
    source .venv/bin/activate
    uv sync
    ```

3. Run example tests
    ```bash
    uv run pytest
    ```