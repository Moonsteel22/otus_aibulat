from queue import Queue
import time

import pytest

from otus_aibulat.exceptions.exceptions_handler import ExceptionHandler
from otus_aibulat.exceptions.handler_commands import PutLoggerExceptionHandlerCommand
from otus_aibulat.exceptions.repeater_command import RepeaterCommand
from otus_aibulat.interfaces import ICommand


class TestCommand:
    def execute(self):
        raise KeyError()

    def __str__(self):
        return "TestCommand"


@pytest.fixture(name="queue")
def _queue() -> Queue:
    _queue: Queue = Queue()
    _queue.put_nowait(TestCommand())
    return _queue


@pytest.fixture(name="ex_handler")
def _ex_handler(queue: Queue) -> ExceptionHandler:
    ex_handler = ExceptionHandler(queue=queue)
    ex_handler.exception_handlers[RepeaterCommand] = {
        Exception: lambda exc, command: PutLoggerExceptionHandlerCommand(
            queue=queue, ex=exc, cmd=command
        )
    }
    ex_handler.exception_handlers[TestCommand] = {
        Exception: lambda exc, command: PutLoggerExceptionHandlerCommand(
            queue=queue, ex=exc, cmd=command
        )
    }
    return ex_handler


def test_run_loop(queue: Queue, ex_handler: ExceptionHandler):
    while not queue.empty():
        cmd: ICommand = queue.get_nowait()
        time.sleep(1)
        try:
            cmd.execute()
        except Exception as ex:
            ex_handler.handle(ex=ex, command=cmd).execute()
