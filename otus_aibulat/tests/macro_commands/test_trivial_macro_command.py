from typing import Any
from unittest.mock import Mock

import pytest

from otus_aibulat.macrocommands.trivial_macro_command import (
    TrivialMacroCommand,
    CommandException,
)


def test_trivial_macro_command_ok() -> None:
    commands: tuple[Any, ...] = tuple(Mock() for _ in range(5))

    macro_command: TrivialMacroCommand = TrivialMacroCommand(commands)

    macro_command.execute()

    for command in commands:
        command.execute.assert_called_once()


def test_trivial_macro_command_error() -> None:
    commands: tuple[Any, ...] = tuple(
        Mock(**{"execute.side_effect": Exception}) for _ in range(5)
    )

    macro_command: TrivialMacroCommand = TrivialMacroCommand(commands)

    with pytest.raises(CommandException):
        macro_command.execute()
