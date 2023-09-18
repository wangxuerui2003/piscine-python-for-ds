def ft_tqdm(lst: range) -> None:
    """
        Print the progress bar every 5% by inputtin a range object
    """

    percentage = 0
    for i in lst:
        percentage = int(round(i / lst.stop, 2) * 100)
        p_bar = '=' * percentage + '>'
        p_bar = p_bar + (' ' * (100 - percentage))

        # only print when its the next 5%
        if percentage % 5 == 0:
            print(f'\r{percentage:>3}%|[{p_bar}]| {i}/{lst.stop}', end='')
        yield i

    if percentage != 0:
        percentage = 100

    p_bar = '=' * percentage + '>'
    print(f'\r{percentage:>3}%|[{p_bar}]| {lst.stop}/{lst.stop}', end='')
