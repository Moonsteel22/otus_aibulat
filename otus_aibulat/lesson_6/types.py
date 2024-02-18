import dataclasses
from typing import TypedDict

@dataclasses.dataclass
class Direction:
    directions_number: float
    direction: float

    def next(self, angular_velocity: float) -> "Direction":
        self.direction = (self.direction + angular_velocity) % self.directions_number

        return self


@dataclasses.dataclass
class Vector:
    x: float
    y: float

    @classmethod
    def plus(cls, first: "Vector", second: "Vector") -> "Vector":
        return Vector(
            x=first.x+second.x,
            y=first.y+second.y
        )


class SpaceObject(TypedDict):
    angular_velocity: float
    location: Vector
    velocity: int
    direction: Direction
