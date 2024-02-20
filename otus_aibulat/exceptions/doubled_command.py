from otus_aibulat.interfaces import ICommand


class DoubledCommand:
    def __init__(self, ex: Exception, cmd: ICommand) -> None:
        self.ex: Exception = ex
        self.cmd: ICommand = cmd

    def execute(self) -> None:
        print(f"[{self}]: Try 2 times [{self.cmd}]")
        try:
            self.cmd.execute()
        except Exception:
            self.cmd.execute()

    def __str__(self) -> str:
        return "DoubleCommand"
