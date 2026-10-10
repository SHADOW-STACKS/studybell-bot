# Decisions

Short log of project decisions, newest first. Decisions that need more
context or trade-off discussion get their own ADR in `docs/adr/` and are linked here.

| Date | Decision | Why |
| ---- | -------- | --- |
| 2026-10-10 | Bot runs on aiogram long polling, started with `python -m app` | No public URL or webhook setup needed for development and demo |
| 2026-10-05 | Issues tracked in GitHub Issues; changes land via PR only | Repo rule on `main` requires pull requests |
