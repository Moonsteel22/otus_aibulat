from typing import Any
from unittest.mock import Mock, call

from otus_aibulat.exceptions.doubled_command import DoubledCommand
from otus_aibulat.exceptions.handler_commands import (
    DoubleAndLogExceptionHandlerCommand,
    PutLoggerExceptionHandlerCommand,
)
from otus_aibulat.exceptions.logger_command import LoggerCommand
from otus_aibulat.exceptions.repeater_command import RepeaterCommand


def test_handler_and_log_command_for_doubled() -> None:
    mock: Any = Mock()
    command_maker: Any = Mock()

    doubled_command: DoubledCommand = DoubledCommand(ex=mock, cmd=mock)
    command: DoubleAndLogExceptionHandlerCommand = DoubleAndLogExceptionHandlerCommand(
        ex=mock, cmd=doubled_command, queue=Mock(), command_maker=command_maker
    )
    command.execute()

    assert command_maker.mock_calls == [
        call(ex=mock, cmd=doubled_command, cmd_class=LoggerCommand),
        call().execute(),
    ]


def test_handler_and_doubled_command_for_doubled() -> None:
    mock: Any = Mock()
    command_maker: Any = Mock(return_value=mock)
    queue: Any = Mock()

    command: DoubleAndLogExceptionHandlerCommand = DoubleAndLogExceptionHandlerCommand(
        ex=mock, cmd=mock, queue=queue, command_maker=command_maker
    )
    command.execute()

    assert command_maker.mock_calls == [
        call(ex=mock, cmd=mock, cmd_class=DoubledCommand)
    ]
    assert queue.put_nowait.mock_calls == [call(mock)]


def test_put_logger_handler_repeater() -> None:
    mock: Any = Mock()
    command_maker: Any = Mock()

    command: PutLoggerExceptionHandlerCommand = PutLoggerExceptionHandlerCommand(
        ex=mock, cmd=mock, command_maker=command_maker
    )
    command.execute()

    assert command_maker.mock_calls == [
        call(ex=mock, cmd=mock, cmd_class=RepeaterCommand),
        call().execute(),
    ]


def test_put_logger_handler_logger() -> None:
    mock: Any = Mock()
    command_maker: Any = Mock()

    repeater_command: RepeaterCommand = RepeaterCommand(ex=mock, cmd=mock)
    command: PutLoggerExceptionHandlerCommand = PutLoggerExceptionHandlerCommand(
        ex=mock, cmd=repeater_command, command_maker=command_maker
    )
    command.execute()

    assert command_maker.mock_calls == [
        call(ex=mock, cmd=repeater_command, cmd_class=LoggerCommand),
        call().execute(),
    ]
