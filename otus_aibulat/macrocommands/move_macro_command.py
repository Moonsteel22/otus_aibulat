from otus_aibulat.macrocommands.trivial_macro_command import TrivialMacroCommand
from otus_aibulat.operations.burnable import BurnFuelCommand
from otus_aibulat.operations.fuel_checkable import CheckFuelCommand
from otus_aibulat.operations.movable import MoveCommand


class MoveMacroCommand(TrivialMacroCommand):
    def __init__(self, commands: tuple[CheckFuelCommand, MoveCommand, BurnFuelCommand]):
        super().__init__(commands=commands)
