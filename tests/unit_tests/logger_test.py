import logging

import pytest

from carnage.logger import setup_logger_handler


@pytest.mark.parametrize(
    ("debug", "expected"),
    (
        (True, False),
        (False, False),
    ),
)
def test_setup_logger_handler(debug, expected):
    setup_logger_handler(debug)
    logger = logging.getLogger("test")
    assert logger.isEnabledFor(logging.DEBUG) == expected
