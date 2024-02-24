from typing import Any
from unittest.mock import Mock

from faker import Faker

from otus_aibulat.operations.burnable.adapter import FuelBurnableAdapter


def test_burnable_adapter(faker: Faker) -> None:
    fuel: int = faker.pyint()
    burnable: Any = Mock(fuel=fuel)
    adapter: FuelBurnableAdapter = FuelBurnableAdapter(burnable_object=burnable)

    adapter.burn()
    assert burnable.fuel == fuel - 1
