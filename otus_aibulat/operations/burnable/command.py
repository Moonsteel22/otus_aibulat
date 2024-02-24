from otus_aibulat.operations.burnable.interfaces import Burnable


class BurnFuelCommand:
    def __init__(self, adapter: Burnable):
        self.adapter: Burnable = adapter

    def execute(self) -> None:
        self.adapter.burn()
