from __future__ import annotations

from contextlib import contextmanager

import pytest
from src.core.settings import Settings
from src.execute import runner


class FakeDriver:
    pass


@pytest.mark.unit
def test_run_crm_smoke_calls_flow(monkeypatch) -> None:
    called: list[str] = []

    @contextmanager
    def fake_build_driver(_settings: Settings):
        yield FakeDriver()

    def fake_flow(driver, settings):  # noqa: ANN001
        assert isinstance(driver, FakeDriver)
        assert settings.run_id == 'unit'
        called.append('ok')

    monkeypatch.setattr(runner, 'build_driver', fake_build_driver)
    monkeypatch.setattr(runner, 'crm_smoke', fake_flow)

    settings = Settings(
        crm_base_url='https://crm.example.test',
        crm_username=None,
        crm_password=None,
        crm_expected_title_contains=None,
        selenium_remote_url='http://localhost:4444/wd/hub',
        selenium_headless=True,
        run_id='unit',
    )

    import asyncio

    asyncio.run(runner.run_crm_smoke(settings))
    assert called == ['ok']
