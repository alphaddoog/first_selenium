from __future__ import annotations

import os
from dataclasses import dataclass


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    raw_norm = raw.strip().lower()
    return raw_norm in {'1', 'true', 't', 'yes', 'y', 'on'}


@dataclass(frozen=True, slots=True)
class Settings:
    crm_base_url: str
    crm_username: str | None
    crm_password: str | None
    crm_expected_title_contains: str | None
    selenium_remote_url: str
    selenium_headless: bool
    run_id: str

    @classmethod
    def from_env(cls) -> 'Settings':
        crm_base_url = os.getenv('CRM_BASE_URL', '').strip()
        selenium_remote_url = os.getenv('SELENIUM_REMOTE_URL', '').strip()

        if not selenium_remote_url:
            selenium_remote_url = 'http://localhost:4444/wd/hub'

        return cls(
            crm_base_url=crm_base_url,
            crm_username=os.getenv('CRM_USERNAME'),
            crm_password=os.getenv('CRM_PASSWORD'),
            crm_expected_title_contains=(
                os.getenv('CRM_EXPECTED_TITLE_CONTAINS') or None
            ),
            selenium_remote_url=selenium_remote_url,
            selenium_headless=_env_bool('SELENIUM_HEADLESS', True),
            run_id=os.getenv('RUN_ID', 'local'),
        )
