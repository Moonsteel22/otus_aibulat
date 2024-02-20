from queue import Queue
from typing import Type, Callable

from otus_aibulat.exceptions.doubled_command import DoubledCommand
from otus_aibulat.exceptions.handler_commands import (
    PutLoggerExceptionHandlerCommand,
    DoubleAndLogExceptionHandlerCommand,
)
from otus_aibulat.exceptions.logger_command import LoggerCommand
from otus_aibulat.exceptions.repeater_command import RepeaterCommand
from otus_aibulat.interfaces import ICommand
from otus_aibulat.movable.command import MoveCommand


class ExceptionHandler:
    exception_handlers: dict[
        Type[ICommand], dict[Type[Exception], Callable[[Exception, ICommand], ICommand]]
    ]

    def __init__(self, queue: Queue) -> None:
        self.exception_handlers = {
            MoveCommand: {
                ValueError: lambda ex, cmd: LoggerCommand(ex=ex, cmd=cmd),
                TypeError: lambda ex, cmd: PutLoggerExceptionHandlerCommand(
                    ex=ex, cmd=cmd
                ),
                KeyError: lambda ex, cmd: DoubleAndLogExceptionHandlerCommand(
                    queue=queue, ex=ex, cmd=cmd
                ),
                Exception: lambda ex, cmd: RepeaterCommand(ex=ex, cmd=cmd),
            },
            DoubledCommand: {
                Exception: lambda ex, cmd: DoubleAndLogExceptionHandlerCommand(
                    queue=queue, ex=ex, cmd=cmd
                )
            },
        }

    def handle(self, ex: Exception, command: ICommand) -> ICommand:
        # Get custom exception handler for command or default for Exception if first one doesn't exist
        return self.exception_handlers[type(command)].get(
            type(ex), self.exception_handlers[type(command)][Exception]
        )(ex, command)
