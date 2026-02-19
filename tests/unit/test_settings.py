from __future__ import annotations

import pytest
from src.core.settings import Settings


@pytest.mark.unit
def test_settings_defaults(monkeypatch) -> None:
    monkeypatch.delenv('SELENIUM_REMOTE_URL', raising=False)
    monkeypatch.delenv('SELENIUM_HEADLESS', raising=False)
    monkeypatch.delenv('RUN_ID', raising=False)
    monkeypatch.delenv('CRM_EXPECTED_TITLE_CONTAINS', raising=False)

    settings = Settings.from_env()

    assert settings.selenium_remote_url == 'http://localhost:4444/wd/hub'
    assert settings.selenium_headless is True
    assert settings.run_id == 'local'


@pytest.mark.unit
def test_env_bool(monkeypatch) -> None:
    monkeypatch.setenv('SELENIUM_HEADLESS', '0')
    assert Settings.from_env().selenium_headless is False

    monkeypatch.setenv('SELENIUM_HEADLESS', 'true')
    assert Settings.from_env().selenium_headless is True
