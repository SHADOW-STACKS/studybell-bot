## Engineering rules

Rules live in `docs/agents/rules/`, tool-neutral Markdown. Levels (`[MUST]`,
`[MUST-UNLESS]`, `[PREFER]`) are defined in `_LEVELS.md`. Always applied:

@docs/agents/rules/_LEVELS.md
@docs/agents/rules/python-core.md

Read the rest before working in their area:

| Area | File |
| ---- | ---- |
| CI workflows, Makefile targets used by CI | `docs/agents/rules/ci-pipeline.md` |
| Tests, fixtures, coverage | `docs/agents/rules/testing.md` |
| Settings, `.env.example`, secrets in logs | `docs/agents/rules/config-hygiene.md` |
| README, decisions log | `docs/agents/rules/documentation.md` |
| FastAPI service, async SQLAlchemy, migrations | `docs/agents/rules/backend-fastapi.md` |
| `frontend/` (Vue 3 + TypeScript) | `docs/agents/rules/frontend-vue.md` |

`docs/agents/rules/clean-architecture.md` is not applied: the project uses the
lighter layering from `backend-fastapi.md`.

## Agent skills

### Issue tracker

Issues live in GitHub Issues (SHADOW-STACKS/studybell-bot), via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-label vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
