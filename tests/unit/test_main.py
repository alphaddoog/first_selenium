from __future__ import annotations

import pytest
import src.__main__ as app_main
from src.core.settings import Settings


@pytest.mark.unit
def test_main_invokes_runner(monkeypatch) -> None:
    called: list[str] = []

    def fake_from_env() -> Settings:
        return Settings(
            crm_base_url='https://crm.example.test',
            crm_username=None,
            crm_password=None,
            crm_expected_title_contains=None,
            selenium_remote_url='http://localhost:4444/wd/hub',
            selenium_headless=True,
            run_id='unit',
        )

    async def fake_run(_settings: Settings) -> None:
        called.append('ok')

    monkeypatch.setattr(app_main.Settings, 'from_env', staticmethod(fake_from_env))
    monkeypatch.setattr(app_main, 'run_crm_smoke', fake_run)

    app_main.main()
    assert called == ['ok']
