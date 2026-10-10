from __future__ import annotations

from aiogram.enums import ParseMode
from pydantic import SecretStr

from app.config import Settings
from app.main import create_bot, create_dispatcher


def test_create_dispatcher_attaches_common_router() -> None:
    assert [router.name for router in create_dispatcher().sub_routers] == ["common"]


def test_create_bot_uses_html_parse_mode() -> None:
    settings = Settings(_env_file=None, bot_token=SecretStr("123456:TEST"))

    assert create_bot(settings).default.parse_mode == ParseMode.HTML
