def square(x: int | float) -> int | float:
    """Square a number and return it"""
    if not isinstance(x, (int, float)):
        print("Argument wrong data type ")
        return -1

    return x ** 2


def pow(x: int | float) -> int | float:
    """Take the exponentiation of the argument itself and return it"""
    if not isinstance(x, (int, float)):
        print("Argument wrong data type ")
        return -1

    return x ** x


def outer(x: int | float, function) -> object:
    """
        A closure that returns an inner function
        that calls the function passed in with the argument x.
    """

    count = 0

    def inner() -> float:
        """Inner function"""
        nonlocal count
        count += 1

        res = x
        for _ in range(count):
            res = function(res)
        return res
    return inner
