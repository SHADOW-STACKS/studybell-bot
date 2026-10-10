from __future__ import annotations

from app.services.help import HELP_TEXT, build_start_text


def test_build_start_text_with_name_greets_by_escaped_name() -> None:
    assert build_start_text("<Ann>") == f"Привет, &lt;Ann&gt;!\n\n{HELP_TEXT}"


def test_build_start_text_without_name_greets_plainly() -> None:
    assert build_start_text(None) == f"Привет!\n\n{HELP_TEXT}"
