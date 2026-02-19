from __future__ import annotations

import pytest
from src.automation.flows.crm_smoke import crm_smoke
from src.core.settings import Settings


class FakeDriver:
    def __init__(self, *, title: str = '') -> None:
        self._title = title
        self.got: list[str] = []

    @property
    def title(self) -> str:
        return self._title

    def get(self, url: str) -> None:
        self.got.append(url)


@pytest.mark.unit
def test_crm_smoke_requires_base_url() -> None:
    settings = Settings(
        crm_base_url='',
        crm_username=None,
        crm_password=None,
        crm_expected_title_contains=None,
        selenium_remote_url='http://localhost:4444/wd/hub',
        selenium_headless=True,
        run_id='unit',
    )
    driver = FakeDriver()

    with pytest.raises(ValueError, match='CRM_BASE_URL'):
        crm_smoke(driver, settings)


@pytest.mark.unit
def test_crm_smoke_opens_base_url() -> None:
    settings = Settings(
        crm_base_url='https://crm.example.test/login',
        crm_username=None,
        crm_password=None,
        crm_expected_title_contains=None,
        selenium_remote_url='http://localhost:4444/wd/hub',
        selenium_headless=True,
        run_id='unit',
    )
    driver = FakeDriver()

    crm_smoke(driver, settings)
    assert driver.got == ['https://crm.example.test/login']


@pytest.mark.unit
def test_crm_smoke_title_check() -> None:
    settings = Settings(
        crm_base_url='https://crm.example.test/login',
        crm_username=None,
        crm_password=None,
        crm_expected_title_contains='Login',
        selenium_remote_url='http://localhost:4444/wd/hub',
        selenium_headless=True,
        run_id='unit',
    )

    driver_ok = FakeDriver(title='CRM - Login')
    crm_smoke(driver_ok, settings)

    driver_bad = FakeDriver(title='Home')
    with pytest.raises(AssertionError, match='Expected title'):
        crm_smoke(driver_bad, settings)
