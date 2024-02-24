from otus_aibulat.operations.burnable.interfaces import BurnableObject


class FuelBurnableAdapter:
    def __init__(self, burnable_object: BurnableObject) -> None:
        self.burnable_object: BurnableObject = burnable_object

    def burn(self) -> None:
        self.burnable_object.fuel -= 1
