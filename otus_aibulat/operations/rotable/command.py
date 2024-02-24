from otus_aibulat.operations.rotable.interfaces import IRotable


class RotateCommand:
    def __init__(self, rotable: IRotable) -> None:
        self.rotable: IRotable = rotable

    def execute(self) -> None:
        self.rotable.set_direction(
            new_value=self.rotable.get_direction().next(
                self.rotable.get_angular_velocity()
            )
        )
