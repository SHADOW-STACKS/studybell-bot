"""Application settings: the only place that reads the environment."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(".env")

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    """Typed settings, read from environment variables and ``.env``."""

    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")

    bot_token: SecretStr
    log_level: LogLevel = "INFO"


def load_settings(env_file: Path | None = ENV_FILE) -> Settings:
    """Build settings once at startup; exit with the variable names on error.

    Only the names of broken variables go into the message, never their values,
    so a mistyped token does not end up in a terminal or a log.
    """
    try:
        return Settings(_env_file=env_file)
    except ValidationError as exc:
        names = sorted({str(error["loc"][0]).upper() for error in exc.errors()})
        raise SystemExit(
            f"Configuration error, check these variables: {', '.join(names)}"
        ) from None
