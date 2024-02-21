import math
from faker import Faker
from otus_aibulat.types import Direction, SpaceObject, Vector
import pytest


@pytest.fixture(name="faker")
def _faker() -> Faker:
    return Faker()


@pytest.fixture(name="velocity")
def _velocity(faker: Faker) -> int:
    return faker.pyint()


@pytest.fixture(name="angular_velocity")
def _angular_velocity() -> float:
    return math.pi


@pytest.fixture(name="direction")
def _direction() -> Direction:
    return Direction(directions_number=2 * math.pi, direction=0.0)


@pytest.fixture(name="location")
def _return_location() -> Vector:
    return Vector(x=12, y=5)


@pytest.fixture(name="space_object")
def _space_object(
    angular_velocity: float, direction: Direction, velocity: int, location: Vector
) -> SpaceObject:
    return SpaceObject(
        angular_velocity=angular_velocity,
        location=location,
        velocity=velocity,
        direction=direction,
    )
