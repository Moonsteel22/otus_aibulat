from otus_aibulat.interfaces import ICommand


class RepeaterCommand:
    def __init__(self, ex: Exception, cmd: ICommand) -> None:
        self.ex: Exception = ex
        self.cmd: ICommand = cmd

    def execute(self) -> None:
        print(f"[{self}]: repeat [{self.cmd}]")
        self.cmd.execute()

    def __str__(self) -> str:
        return "RepeaterCommand"
