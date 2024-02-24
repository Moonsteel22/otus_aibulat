from typing import Protocol


class IFuelContainsObject(Protocol):
    fuel: int


class ICheckFuelAdapter(Protocol):
    def check_fuel(self) -> None:
        ...
