from typing import Any
from unittest.mock import Mock

import pytest

from otus_aibulat.exceptions.doubled_command import DoubledCommand


def test_doubled_command() -> None:
    exception: Any = Mock()
    command: Any = Mock(**{"execute.side_effect": Exception})

    doubled_command: DoubledCommand = DoubledCommand(ex=exception, cmd=command)

    with pytest.raises(Exception):
        doubled_command.execute()

    assert command.execute.call_count == 2
