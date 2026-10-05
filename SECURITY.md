# Security Policy

## Supported versions

Only the latest commit on `main` is supported until the first tagged release.

## Reporting a vulnerability

Do not open a public issue for security problems.

Report privately via GitHub: **Security → Report a vulnerability**
(https://github.com/SHADOW-STACKS/studybell-bot/security/advisories/new).

Include what you found, steps to reproduce, and the impact. You can expect an
acknowledgement within 7 days.

## Handling secrets

- Never commit bot tokens, API keys, or `.env` files.
- If a token leaks, revoke and regenerate it immediately, then report it as above.
