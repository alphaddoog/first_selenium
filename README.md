# hub-automation-integration-api
Automação assíncrona

## Como rodar local (unit)

```bash
poetry install
poetry run task test_unit
```

## Como rodar integração via Docker (Selenium + pytest)

1) Copie o arquivo de exemplo:

```bash
cp .env.test.example .env.test
```

2) Ajuste `CRM_BASE_URL` (e credenciais se necessário).

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
