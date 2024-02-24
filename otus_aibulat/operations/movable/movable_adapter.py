import math

from otus_aibulat.operations.movable.exceptions import (
    GetLocationException,
    GetVelocityException,
    SetLocationException,
)
from otus_aibulat.types import SpaceObject, Vector
from otus_aibulat.utils import raise_exception


class MovableAdapter:
    def __init__(self, space_object: SpaceObject) -> None:
        self.space_object: SpaceObject = space_object

    @raise_exception(
        exception=GetLocationException, message="Can't get location of movable"
    )
    def get_location(self) -> Vector:
        return self.space_object["location"]

    @raise_exception(
        exception=GetVelocityException, message="Can't get velocity of movable"
    )
    def get_velocity(self) -> Vector:
        velocity: int = self.space_object["velocity"]
        direction: float = self.space_object["direction"].direction

        return Vector(
            x=velocity * math.cos(direction), y=velocity * math.sin(direction)
        )

    @raise_exception(
        exception=SetLocationException, message="Can't set location for movable"
    )
    def set_location(self, value: Vector) -> None:
        self.space_object["location"] = value
