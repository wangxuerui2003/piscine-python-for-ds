def ft_filter(func, lst) -> list[str]:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if func is None:
        return [item for item in lst if item]
    return [item for item in lst if func(item)]
