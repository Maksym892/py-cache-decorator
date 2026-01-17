import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # Write your code here
    cashe_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        keyword = ""
        for arg in args:
            keyword += str(arg)
        if keyword in cashe_dict.keys():
            print("Getting from cache ")
        else:
            print("Calculating new result")
            cashe_dict[keyword] = func(*args, **kwargs)
        return cashe_dict[keyword]
    return wrapper
