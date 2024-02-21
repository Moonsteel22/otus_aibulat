from typing import Protocol

from otus_aibulat.interfaces import ICommand


class Logger(Protocol):
    def __call__(self, msg: str) -> None:
        ...


class LoggerCommand:
    def __init__(
        self, ex: Exception, cmd: ICommand, logger_func: Logger = lambda msg: print(msg)
    ) -> None:
        self.ex: Exception = ex
        self.cmd: ICommand = cmd
        self.logger: Logger = logger_func

    def execute(self) -> None:
        self.logger(
            msg=f"[{self}]: {self.ex} exception from {self.cmd} has been raised!"
        )

    def __str__(self) -> str:
        return "LoggerCommand"
