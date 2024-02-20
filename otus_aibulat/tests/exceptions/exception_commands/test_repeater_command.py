from typing import Any
from unittest.mock import Mock

from otus_aibulat.exceptions.repeater_command import RepeaterCommand


def test_repeater_command() -> None:
    exception: Any = Mock()
    command: Any = Mock()

    repeater_command: RepeaterCommand = RepeaterCommand(ex=exception, cmd=command)

    repeater_command.execute()

    assert command.execute.call_count == 1
