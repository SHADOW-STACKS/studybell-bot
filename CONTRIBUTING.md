# Contributing

## Workflow

1. Open or pick an issue (new issues are labelled `needs-triage`).
2. Branch from `main`: `<type>/<short-description>`, e.g. `feat/reminder-command`.
3. Make the smallest change that solves the problem; don't mix in unrelated refactors.
4. Run the project checks (linter, type checker, tests) and make sure they pass.
5. Open a pull request against `main`. Direct pushes to `main` are blocked, and PRs need a review before merging.

## Commits

Small, frequent commits with an imperative subject line, e.g. `Add reminder command`.

## Development setup

<!-- TODO: requirements, install, how to run checks. -->

## Configuration

Copy `.env.example` to `.env` and fill in the values. Never commit `.env`.

## Reporting security issues

See [SECURITY.md](SECURITY.md). Do not use public issues for these.

## Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
