import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # Write your code here
    cashe_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        keyword = (args, tuple(kwargs.items()))
        if keyword in cashe_dict:
            print("Getting from cache ")
            return cashe_dict[keyword]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cashe_dict[keyword] = result
        return result

    return wrapper
