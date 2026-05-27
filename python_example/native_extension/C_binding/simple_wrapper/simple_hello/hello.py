from . import _hello_core


class Hello:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return _hello_core.make_greeting(self.name)


def print_hello() -> None:
    _hello_core.print_hello()
