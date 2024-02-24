from typing import Any
from unittest.mock import Mock

import pytest

from otus_aibulat.operations.fuel_checkable import NotFuelException
from otus_aibulat.operations.fuel_checkable.adapter import CheckFuelAdapter


@pytest.mark.parametrize("fuel", [i for i in range(1, 5)])
def test_fuel_checkable_adapter_ok(fuel: int) -> None:
    fuel_contains_object: Any = Mock(fuel=fuel)

    adapter: CheckFuelAdapter = CheckFuelAdapter(fuel_object=fuel_contains_object)

    adapter.check_fuel()


@pytest.mark.parametrize("fuel", (-1, -100, 0))
def test_fuel_checkable_adapter_error(fuel: int) -> None:
    fuel_contains_object: Any = Mock(fuel=fuel)

    adapter: CheckFuelAdapter = CheckFuelAdapter(fuel_object=fuel_contains_object)

    with pytest.raises(NotFuelException):
        adapter.check_fuel()
