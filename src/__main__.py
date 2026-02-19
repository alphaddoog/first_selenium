from __future__ import annotations

import asyncio

from src.core.settings import Settings
from src.execute.runner import run_crm_smoke


def main() -> None:
    settings = Settings.from_env()
    asyncio.run(run_crm_smoke(settings))


if __name__ == '__main__':
    main()
