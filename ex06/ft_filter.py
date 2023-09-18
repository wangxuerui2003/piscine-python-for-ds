def ft_filter(func, words) -> list[str]:
    """
        Returns a list of words which satisfies the func
    """

    return [word for word in words if func(word)]
