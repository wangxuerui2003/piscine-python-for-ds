def ft_tqdm(lst: range) -> None:
    """
        Print the progress bar by inputting a range object
    """

    stop = lst.stop - lst.start
    percentage = 0
    for i in lst:
        i -= lst.start
        percentage = int(round(i / stop, 2) * 100)
        p_bar = '=' * percentage + '>'
        p_bar = p_bar + (' ' * (100 - percentage))

        print(f'\r{percentage:>3}%|[{p_bar}]| {i}/{stop}', end='')
        yield i

    if percentage != 0:
        percentage = 100

    p_bar = '=' * percentage + '>'
    print(f'\r{percentage:>3}%|[{p_bar}]| {stop}/{stop}', end='')
