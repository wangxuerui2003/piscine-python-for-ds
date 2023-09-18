from typing import Iterable, Callable


def ft_filter(func: Callable, words: Iterable) -> list[str]:
    return [word for word in words if func(word)]
