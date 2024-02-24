from otus_aibulat.operations.fuel_checkable.exceptions import NotFuelException
from otus_aibulat.operations.fuel_checkable.interfaces import IFuelContainsObject


class CheckFuelAdapter:
    def __init__(self, fuel_object: IFuelContainsObject) -> None:
        self.fuel_object: IFuelContainsObject = fuel_object

    def check_fuel(self) -> None:
        if self.fuel_object.fuel <= 0:
            raise NotFuelException(f"There is no fuel for {self.fuel_object}")
