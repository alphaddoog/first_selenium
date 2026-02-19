# hub-automation-integration-api
Automação assíncrona com **testes de integração** contra um CRM (via Selenium remoto).

## Objetivo

- Executar automações de forma **assíncrona** (orquestração via `asyncio`).
- Ter uma base sólida de **unit tests** (rápidos, determinísticos, com cobertura alta).
- Rodar **integration tests** de forma reprodutível via **Docker + Selenium**.

## Estrutura do projeto

```
.
├── src/
│   ├── __main__.py                    # entrypoint: `python -Om src`
│   ├── core/
│   │   ├── settings.py                # leitura de env (CRM/Selenium)
│   │   └── config/logging.py
│   ├── builder/
│   │   └── selenium_driver.py         # WebDriver remoto (Remote)
│   ├── automation/
│   │   └── flows/
│   │       └── crm_smoke.py           # fluxo básico (smoke)
│   └── execute/
│       └── runner.py                  # runner async (to_thread)
├── tests/
│   ├── unit/                          # testes unitários
│   └── integration/                   # testes de integração (CRM real)
├── Dockerfile
├── docker-compose.yml                 # selenium + runner de testes
├── .env.test.example                  # template (copie para .env.test)
└── pyproject.toml
```

## Requisitos

- Python `3.13+`
- Poetry `2.x`
- Docker (para rodar integração via Selenium)

## Como rodar local (unit)

```bash
poetry install
poetry run task test_unit
```

## Rodar o runner (manual)

```bash
poetry run task run
```

## Como rodar integração via Docker (Selenium + pytest)

1) Copie o arquivo de exemplo para criar o seu `.env.test` (não commitar):

```bash
cp .env.test.example .env.test
```

2) Ajuste `CRM_BASE_URL` (e credenciais se necessário) no `.env.test`.

3) Suba e rode:

```bash
docker compose --env-file .env.test up --build --abort-on-container-exit
```

## Variáveis de ambiente (integração)

- `CRM_BASE_URL` (obrigatório para integração)
- `CRM_USERNAME` / `CRM_PASSWORD` (opcional)
- `CRM_EXPECTED_TITLE_CONTAINS` (opcional; valida título da página)
- `SELENIUM_REMOTE_URL` (ex.: `http://selenium:4444/wd/hub`)
- `SELENIUM_HEADLESS` (`1`/`0`)
- `RUN_ID` (tag para rastrear dados)

## Marcadores de testes (pytest)

- `unit`: testes unitários
- `integration`: testes de integração (dependem de CRM + Selenium)
- `need_dot_env`: testes que consultam `.env.test`

Comandos úteis:

```bash
poetry run pytest tests -m "unit" -vv
poetry run pytest tests -m "integration" --no-cov -vv
```

## CI (GitHub Actions)

- O job **unit** roda em todo `push`/`pull_request`.
- O job **integration** está configurado para rodar apenas em `workflow_dispatch` e usa **Secrets**:
  - `CRM_BASE_URL`, `CRM_USERNAME`, `CRM_PASSWORD`, `CRM_EXPECTED_TITLE_CONTAINS`

## Troubleshooting rápido

- **Integração foi “skipped”**: verifique se `CRM_BASE_URL` e `SELENIUM_REMOTE_URL` estão definidos.
- **Selenium não conecta**:
  - Local: `SELENIUM_REMOTE_URL="http://localhost:4444/wd/hub"`
  - Docker compose: `SELENIUM_REMOTE_URL="http://selenium:4444/wd/hub"`
- **Testes flakey**: prefira waits explícitos, timeouts coerentes e capture artifacts (screenshot/HTML) ao falhar.
