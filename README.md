# studybell-bot

Telegram bot that reminds students about deadlines, schedules and events.
Stack: Python 3.13, aiogram 3 (long polling), pydantic-settings; SQLAlchemy,
Alembic and APScheduler are declared for the upcoming features.

## Status

Early development. The bot starts and answers `/start` and `/help`; events and
reminders are not implemented yet.

## Prerequisites

- Python 3.13 (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) >= 0.12.11
- GNU Make (optional, wraps the commands below)

## Run locally

```bash
uv sync --locked --all-extras
cp .env.example .env   # then put your token from @BotFather into BOT_TOKEN
uv run python -m app
```

## Configuration

Settings are read from environment variables and `.env` by one settings object
(`app/config.py`); see [`.env.example`](.env.example) for the template.

| Variable | Default | When to change |
| -------- | ------- | -------------- |
| `BOT_TOKEN` | — (required) | Always: the token of your bot from @BotFather |
| `LOG_LEVEL` | `INFO` | `DEBUG` to see more while developing |

A missing or invalid variable stops the bot at startup with the variable name
in the message; values are never printed.

## Architecture

| Layer | Package | Contents |
| ----- | ------- | -------- |
| Interface | `app/bot/` | aiogram routers and handlers, no business logic |
| Business logic | `app/services/` | texts and, later, events and reminders |
| Data | `app/db/` | placeholder until the first stored model |

`app/main.py` assembles the bot and the dispatcher; `python -m app` runs it.

## Testing

```bash
make check          # lint + format + types + tests
uv run pytest       # tests only
```

Without Make: `uv run ruff check .`, `uv run ruff format --check .`,
`uv run mypy .`, `uv run pytest tests/ -v`. Unit tests live in `tests/unit/`
and need nothing but the installed dependencies.

## Decisions worth knowing

- Long polling, not webhooks: no public URL is needed to run the bot.
- All configuration goes through `app.config.Settings`; a test keeps
  `.env.example` in sync with its fields.

Full log: [docs/decisions.md](docs/decisions.md).

## Next steps

User registration and the database layer, then events and reminders.

## Documentation

- [Security policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Decisions log](docs/decisions.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes to `main` go through a pull request.

## License

[MIT](LICENSE)
