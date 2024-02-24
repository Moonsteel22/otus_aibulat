from otus_aibulat.operations.fuel_checkable.interfaces import ICheckFuelAdapter


class CheckFuelCommand:
    def __init__(self, adapter: ICheckFuelAdapter):
        self.adapter: ICheckFuelAdapter = adapter

    def execute(self) -> None:
        self.adapter.check_fuel()
