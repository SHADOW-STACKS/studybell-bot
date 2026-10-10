"""Texts for the /start and /help commands."""

from __future__ import annotations

from html import escape

HELP_TEXT = (
    "Я StudyBell, бот-напоминалка о дедлайнах, расписании и событиях.\n\n"
    "Команды:\n"
    "/start — начать работу\n"
    "/help — список команд\n\n"
    "Добавление событий и напоминания скоро появятся."
)


def build_start_text(first_name: str | None) -> str:
    """Greeting for /start; the name is HTML-escaped for parse_mode=HTML."""
    greeting = f"Привет, {escape(first_name)}!" if first_name else "Привет!"
    return f"{greeting}\n\n{HELP_TEXT}"
