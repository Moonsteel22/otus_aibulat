
from typing import Callable, Type


def raise_exception(exception: Type[Exception], message: str) -> Callable:
    
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                raise exception(message) from exc
        return inner_wrapper
    return wrapper