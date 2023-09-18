def ft_filter(func, lst) -> list[str]:
    """
        Returns a list of lst which satisfies the func
    """

    if func is None:
        return [item for item in lst if item]
    return [item for item in lst if func(item)]
