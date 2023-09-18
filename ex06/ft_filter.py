from typing import Iterable, Callable


def ft_filter(func: Callable, words: Iterable) -> list[str]:
    """
        Returns a list of words which satisfies the func
    """

    return [word for word in words if func(word)]
