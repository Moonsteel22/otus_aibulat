from typing import Protocol, Type

from otus_aibulat.interfaces import ICommand


class IExceptionCommand(Protocol):
    ex: Exception
    cmd: ICommand

    def execute(self) -> None:
        ...


class CommandMaker(Protocol):
    def __call__(
        self, ex: Exception, cmd: ICommand, cmd_class: Type[ICommand]
    ) -> IExceptionCommand:
        ...
