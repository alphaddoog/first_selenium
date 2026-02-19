from __future__ import annotations

import asyncio

from src.automation.flows.crm_smoke import crm_smoke
from src.builder.selenium_driver import build_driver
from src.core.settings import Settings


async def run_crm_smoke(settings: Settings) -> None:
    def _run() -> None:
        with build_driver(settings) as driver:
            crm_smoke(driver, settings)

    await asyncio.to_thread(_run)
