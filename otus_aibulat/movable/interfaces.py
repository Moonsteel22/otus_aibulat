from typing import Protocol
from otus_aibulat.types import Vector


class IMovable(Protocol):

    def get_location(self) -> Vector:
        ...

    def get_velocity(self) -> Vector:
        ...

    def set_location(self, value: Vector) -> None:
        ...
