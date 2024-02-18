from otus_aibulat.lesson_6.types import Direction, SpaceObject


class RotableAdapter:

    def __init__(self, space_object: SpaceObject) -> None:
        self.space_object: SpaceObject = space_object

    def get_direction(self) -> Direction:
        return self.space_object["direction"]
    
    def get_angular_velocity(self) -> float:
        return self.space_object["angular_velocity"]
    
    def set_direction(self, new_value: Direction) -> None:
        self.space_object["direction"] = new_value