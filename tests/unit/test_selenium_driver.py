from __future__ import annotations

import pytest
from src.builder import selenium_driver
from src.core.settings import Settings


class FakeRemoteDriver:
    def __init__(self) -> None:
        self.quit_called = False

    def quit(self) -> None:
        self.quit_called = True


@pytest.mark.unit
def test_build_driver_quits(monkeypatch) -> None:
    created: list[FakeRemoteDriver] = []

    def fake_remote(*args, **kwargs):  # noqa: ANN001
        driver = FakeRemoteDriver()
        created.append(driver)
        return driver

    monkeypatch.setattr(selenium_driver.webdriver, 'Remote', fake_remote)

    settings = Settings(
        crm_base_url='https://crm.example.test',
        crm_username=None,
        crm_password=None,
        crm_expected_title_contains=None,
        selenium_remote_url='http://localhost:4444/wd/hub',
        selenium_headless=True,
        run_id='unit',
    )

    with selenium_driver.build_driver(settings) as driver:
        assert isinstance(driver, FakeRemoteDriver)

    assert created
    assert created[0].quit_called is True
