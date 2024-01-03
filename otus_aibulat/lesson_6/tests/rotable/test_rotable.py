import math
from faker import Faker
from otus_aibulat.lesson_6.rotable.command import RotateCommand
import pytest

from otus_aibulat.lesson_6.rotable.rotable_adapter import RotableAdapter
from otus_aibulat.lesson_6.types import Direction, SpaceObject, Vector


@pytest.fixture(name="rotable_adapter")
def _rotable_adapter(space_object: SpaceObject) -> RotableAdapter:
    return RotableAdapter(space_object=space_object)


def test_direction(faker: Faker, direction: Direction) -> None:
    test_value: float = faker.pyfloat()

    expected_direction: Direction = Direction(
        direction=(direction.direction+test_value) % direction.directions_number,
        directions_number=direction.directions_number
    )

    assert direction.next(test_value) == expected_direction


def test_rotable_get(rotable_adapter: RotableAdapter, angular_velocity: float, direction: Direction) -> None:

    actual_angular_velocity: float = rotable_adapter.get_angular_velocity()

    assert actual_angular_velocity == angular_velocity

    actual_direction: Direction = rotable_adapter.get_direction()

    assert actual_direction == direction


def test_rotable_set(faker: Faker, rotable_adapter: RotableAdapter, direction: Direction) -> None:

    new_direction: Direction = Direction(direction=faker.pyfloat(), directions_number=faker.pyfloat())

    assert rotable_adapter.space_object["direction"] == direction

    rotable_adapter.set_direction(new_value=new_direction)

    assert rotable_adapter.space_object["direction"] == new_direction


def test_command(rotable_adapter: RotableAdapter, direction: Direction) -> None:
    command: RotateCommand = RotateCommand(rotable=rotable_adapter)

    command.execute()

    assert rotable_adapter.get_direction() == direction.next(rotable_adapter.space_object["angular_velocity"])