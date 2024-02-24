from typing import Iterable

from otus_aibulat.interfaces import ICommand


class CommandException(Exception):
    ...


class TrivialMacroCommand:
    def __init__(self, commands: Iterable[ICommand]):
        self.commands: Iterable[ICommand] = commands

    def execute(self) -> None:
        for command in self.commands:
            try:
                command.execute()
            except Exception as e:
                raise CommandException(e)
