from __future__ import annotations

from pathlib import Path

import pytest

from app.config import Settings, load_settings

ENV_EXAMPLE = Path(__file__).resolve().parents[2] / ".env.example"


def _env_example_keys() -> set[str]:
    lines = ENV_EXAMPLE.read_text(encoding="utf-8").splitlines()
    return {
        line.split("=", 1)[0].strip()
        for line in lines
        if line.strip() and not line.lstrip().startswith("#")
    }


def test_env_example_keys_match_settings_fields() -> None:
    assert _env_example_keys() == {name.upper() for name in Settings.model_fields}


def test_load_settings_without_token_exits_naming_the_variable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("BOT_TOKEN", raising=False)

    with pytest.raises(SystemExit, match="BOT_TOKEN"):
        load_settings(env_file=None)


def test_load_settings_hides_token_in_repr(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT_TOKEN", "123456:secret-value")

    assert "secret-value" not in repr(load_settings(env_file=None))
