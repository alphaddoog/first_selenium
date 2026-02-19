from __future__ import annotations

from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver

from src.core.settings import Settings


def _chrome_options(headless: bool) -> ChromeOptions:
    options = ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1365,768')
    return options


@contextmanager
def build_driver(settings: Settings) -> WebDriver:
    options = _chrome_options(settings.selenium_headless)
    driver = webdriver.Remote(
        command_executor=settings.selenium_remote_url,
        options=options,
    )
    try:
        yield driver
    finally:
        driver.quit()
