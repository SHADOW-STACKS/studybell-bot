from __future__ import annotations

import logging

from app.logging_config import setup_logging


def test_setup_logging_sets_root_level() -> None:
    setup_logging("WARNING")

    assert logging.getLogger().level == logging.WARNING
