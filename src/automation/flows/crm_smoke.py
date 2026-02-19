from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver

from src.core.settings import Settings


def crm_smoke(driver: WebDriver, settings: Settings) -> None:
    if not settings.crm_base_url:
        raise ValueError('CRM_BASE_URL is required for CRM smoke flow')

    driver.get(settings.crm_base_url)

    expected = settings.crm_expected_title_contains
    if expected:
        title = driver.title or ''
        if expected not in title:
            raise AssertionError(
                f'Expected title to contain {expected!r}, got {title!r}',
            )
