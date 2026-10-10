from __future__ import annotations

from dataclasses import dataclass, field
from typing import cast

from aiogram.types import Message

from app.bot.handlers.common import handle_help, handle_start
from app.services.help import HELP_TEXT, build_start_text


@dataclass
class FakeUser:
    id: int
    first_name: str


@dataclass
class FakeMessage:
    """Stands in for the Telegram boundary: records answers instead of sending."""

    from_user: FakeUser | None
    answers: list[str] = field(default_factory=list)

    async def answer(self, text: str) -> None:
        self.answers.append(text)


async def test_handle_start_answers_with_personal_greeting() -> None:
    message = FakeMessage(from_user=FakeUser(id=1, first_name="Аня"))

    await handle_start(cast(Message, message))

    assert message.answers == [build_start_text("Аня")]


async def test_handle_help_answers_with_help_text() -> None:
    message = FakeMessage(from_user=None)

    await handle_help(cast(Message, message))

    assert message.answers == [HELP_TEXT]
