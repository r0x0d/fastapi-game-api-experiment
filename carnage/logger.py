import logging
import logging.config

from rich.logging import RichHandler


def setup_logger_handler(debug: bool) -> None:
    logging.basicConfig(
        level=logging.NOTSET,
        format="%(asctime)s: %(message)s",  # noqa
        datefmt="[%X]",
        handlers=[RichHandler()],
    )
    logger = logging.getLogger("carnage")
    logger.propagate = True

    if not debug:
        logging.disable(logging.DEBUG)
