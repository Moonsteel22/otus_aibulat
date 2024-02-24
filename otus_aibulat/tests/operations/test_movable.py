import math
from unittest.mock import Mock
from faker import Faker
from otus_aibulat.operations.movable.exceptions import (
    GetLocationException,
    GetVelocityException,
    SetLocationException,
)

from otus_aibulat.types import Direction, SpaceObject, Vector
from otus_aibulat.operations.movable import MoveCommand
from otus_aibulat.operations.movable.movable_adapter import MovableAdapter
import pytest


@pytest.fixture(name="movable_adapter")
def _movable_adapter(space_object: SpaceObject) -> MovableAdapter:
    return MovableAdapter(space_object=space_object)


def test_move_get(
    direction: Direction,
    velocity: int,
    location: Vector,
    movable_adapter: MovableAdapter,
) -> None:
    assert movable_adapter.get_location() == location

    expected_velocity: Vector = Vector(
        x=velocity * math.cos(direction.direction),
        y=velocity * math.sin(direction.direction),
    )

    assert movable_adapter.get_velocity() == expected_velocity


def test_move_set(faker: Faker, movable_adapter: MovableAdapter) -> None:
    new_location: Vector = Vector(x=faker.pyint(), y=faker.pyint())

    movable_adapter.set_location(value=new_location)

    assert movable_adapter.space_object["location"] == new_location


def test_move_exceptions(movable_adapter: MovableAdapter) -> None:
    movable_adapter.space_object = Mock(**{"side_effect": KeyError})

    with pytest.raises(GetLocationException):
        movable_adapter.get_location()

    with pytest.raises(GetVelocityException):
        movable_adapter.get_velocity()

    with pytest.raises(SetLocationException):
        movable_adapter.set_location(value=Vector(x=0, y=0))


def test_command(movable_adapter: MovableAdapter) -> None:
    move_command = MoveCommand(movable=movable_adapter)

    movable_adapter.get_velocity = Mock(**{"return_value": Vector(x=-7, y=3)})
    move_command.execute()

    actual_location: Vector = movable_adapter.get_location()
    expected_location: Vector = Vector(5, 8)

    assert actual_location == expected_location
