from queue import Queue
from typing import Type, Callable

from otus_aibulat.exceptions.handler_commands import (
    PutLoggerExceptionHandlerCommand,
)
from otus_aibulat.exceptions.logger_command import LoggerCommand
from otus_aibulat.interfaces import ICommand
from otus_aibulat.operations.movable import MoveCommand


class ExceptionHandler:
    exception_handlers: dict[
        Type[ICommand], dict[Type[Exception], Callable[[Exception, ICommand], ICommand]]
    ]

    def __init__(self, queue: Queue) -> None:
        self.exception_handlers = {
            MoveCommand: {
                Exception: lambda ex, cmd: PutLoggerExceptionHandlerCommand(
                    ex=ex, cmd=cmd, queue=queue
                ),
            },
        }

    def handle(self, ex: Exception, command: ICommand) -> ICommand:
        # Get custom exception handler for command or default for Exception if first one doesn't exist
        if command_type_exceptions := self.exception_handlers.get(type(command)):
            return command_type_exceptions.get(
                type(ex), self.exception_handlers[type(command)][Exception]
            )(ex, command)
        return LoggerCommand(ex=ex, cmd=command)
