from typing import Any
from unittest.mock import Mock

from otus_aibulat.macrocommands.move_macro_command import MoveMacroCommand


def test_move_macro_command() -> None:
    move_command: Any = Mock()
    check_fuel_command: Any = Mock()
    burn_fuel_command: Any = Mock()

    move_macro_command: MoveMacroCommand = MoveMacroCommand(
        commands=(check_fuel_command, move_command, burn_fuel_command)  # порядок важен!
    )

    move_macro_command.execute()

    move_command.execute.assert_called_once()
    check_fuel_command.execute.assert_called_once()
    burn_fuel_command.execute.assert_called_once()
