from queue import Queue

from otus_aibulat.exceptions.doubled_command import DoubledCommand
from otus_aibulat.exceptions.interfaces import CommandMaker
from otus_aibulat.exceptions.logger_command import LoggerCommand
from otus_aibulat.exceptions.repeater_command import RepeaterCommand
from otus_aibulat.interfaces import ICommand


class PutLoggerExceptionHandlerCommand:
    def __init__(
        self,
        ex: Exception,
        cmd: ICommand,
        queue: Queue,
        command_maker: CommandMaker = lambda ex, cmd, cmd_class: cmd_class(ex, cmd),
    ):
        self.ex = ex
        self.cmd = cmd
        self.command_maker = command_maker
        self.queue = queue

    def execute(self) -> None:
        if isinstance(self.cmd, RepeaterCommand):
            print(f"[{self}]: Unsuccessful, just logging...")
            self.command_maker(ex=self.ex, cmd=self.cmd, cmd_class=LoggerCommand)
            return
        self.queue.put_nowait(
            self.command_maker(ex=self.ex, cmd=self.cmd, cmd_class=RepeaterCommand)
        )

    def __str__(self) -> str:
        return "DoubleAndLogExceptionHandlerCommand"


class DoubleAndLogExceptionHandlerCommand:
    def __init__(
        self,
        queue: Queue,
        ex: Exception,
        cmd: ICommand,
        command_maker: CommandMaker = lambda ex, cmd, cmd_class: cmd_class(ex, cmd),
    ):
        self.ex = ex
        self.cmd = cmd
        self.queue = queue
        self.command_maker = command_maker

    def execute(self) -> None:
        if isinstance(self.cmd, DoubledCommand):
            print(f"[{self}]: Unsuccessful, just logging...")
            self.command_maker(
                ex=self.ex, cmd=self.cmd, cmd_class=LoggerCommand
            ).execute()
            return
        print(f"[{self}]: Try one more time [{self.cmd}] and log the exception")
        self.queue.put_nowait(
            self.command_maker(ex=self.ex, cmd=self.cmd, cmd_class=DoubledCommand)
        )

    def __str__(self) -> str:
        return "DoubleAndLogExceptionHandlerCommand"
