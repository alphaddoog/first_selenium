from __future__ import annotations

import os

import pytest
from src.core.settings import Settings


@pytest.fixture(scope='session')
def settings() -> Settings:
    return Settings.from_env()


def pytest_collection_modifyitems(
    config: pytest.Config,
    items: list[pytest.Item],
) -> None:
    crm_base_url = os.getenv('CRM_BASE_URL', '').strip()
    remote_url = os.getenv('SELENIUM_REMOTE_URL', '').strip()

    if crm_base_url and remote_url:
        return

    skip_integration = pytest.mark.skip(
        reason='integration tests require CRM_BASE_URL and SELENIUM_REMOTE_URL',
    )
    for item in items:
        if 'integration' in item.keywords:
            item.add_marker(skip_integration)
