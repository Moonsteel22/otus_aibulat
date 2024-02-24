from otus_aibulat.operations.movable.interfaces import IMovable
from otus_aibulat.types import Vector


class MoveCommand:
    def __init__(self, movable: IMovable) -> None:
        self.movable: IMovable = movable

    def execute(self) -> None:
        self.movable.set_location(
            value=Vector.plus(self.movable.get_location(), self.movable.get_velocity())
        )
