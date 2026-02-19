from __future__ import annotations

import pytest
from src.automation.flows.crm_smoke import crm_smoke
from src.builder.selenium_driver import build_driver
from src.core.settings import Settings


@pytest.mark.integration
@pytest.mark.need_dot_env
def test_crm_smoke_flow(settings: Settings) -> None:
    with build_driver(settings) as driver:
        crm_smoke(driver, settings)
