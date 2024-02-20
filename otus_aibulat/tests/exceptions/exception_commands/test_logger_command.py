from typing import Any
from unittest.mock import Mock, call, MagicMock

from otus_aibulat.exceptions.logger_command import LoggerCommand


def test_logger_command() -> None:
    test_msg: str = "test"
    exception: Any = MagicMock(**{"__str__.return_value": test_msg})
    command: Any = MagicMock(**{"__str__.return_value": test_msg})
    logger: Any = Mock()

    logger_command: LoggerCommand = LoggerCommand(
        ex=exception, cmd=command, logger_func=logger
    )

    msg: str = (
        f"[{logger_command}]: {test_msg} exception from {test_msg} has been raised!"
    )

    logger_command.execute()

    assert logger.mock_calls == [call(msg=msg)]
