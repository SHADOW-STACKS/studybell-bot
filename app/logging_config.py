"""Logging setup for the whole process."""

from __future__ import annotations

import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def setup_logging(level: str) -> None:
    """Configure the root logger once at startup."""
    logging.basicConfig(level=level, format=LOG_FORMAT, force=True)
