from typing import Protocol


class Burnable(Protocol):
    def burn(self) -> None:
        ...


class BurnableObject(Protocol):
    fuel: int
