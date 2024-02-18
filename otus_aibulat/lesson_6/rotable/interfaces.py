from typing import Protocol
from otus_aibulat.lesson_6.types import Direction


class IRotable(Protocol):
    def get_direction(self) -> Direction:
        ...
    
    def get_angular_velocity(self) -> float:
        ...
    
    def set_direction(self, new_value: Direction) -> None:
        ...
