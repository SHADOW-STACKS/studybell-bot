"""Bot assembly and startup."""

from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.handlers.common import create_router
from app.config import Settings, load_settings
from app.logging_config import setup_logging

logger = logging.getLogger(__name__)


def create_dispatcher() -> Dispatcher:
    """Dispatcher with every router attached."""
    dispatcher = Dispatcher()
    dispatcher.include_router(create_router())
    return dispatcher


def create_bot(settings: Settings) -> Bot:
    """Bot client; the token is unwrapped only here."""
    return Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )


async def run(settings: Settings) -> None:
    """Start long polling and close the HTTP session on exit."""
    bot = create_bot(settings)
    logger.info("Bot is starting (long polling)")
    try:
        await create_dispatcher().start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot stopped")


def main() -> None:
    """Process entry point."""
    settings = load_settings()
    setup_logging(settings.log_level)
    asyncio.run(run(settings))
