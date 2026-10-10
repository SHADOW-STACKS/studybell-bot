"""Handlers for /start and /help."""

from __future__ import annotations

import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.services.help import HELP_TEXT, build_start_text

logger = logging.getLogger(__name__)


async def handle_start(message: Message) -> None:
    """Greet the user and list the commands."""
    user = message.from_user
    logger.info("/start from user_id=%s", user.id if user else None)
    await message.answer(build_start_text(user.first_name if user else None))


async def handle_help(message: Message) -> None:
    """List the commands."""
    await message.answer(HELP_TEXT)


def create_router() -> Router:
    """Router with the common commands; a new one per call, so tests can attach it."""
    router = Router(name="common")
    router.message.register(handle_start, CommandStart())
    router.message.register(handle_help, Command("help"))
    return router
