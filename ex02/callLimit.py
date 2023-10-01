def callLimit(limit: int):
    """
        A function that returns a decorator
        which limits the number of calls of a function to "limit".
    """
    count = 0

    def callLimiter(function):
        """The decorator"""
        def limited_function(*args: any, **kwds: any):
            """
                Inner function of the decorator
                which takes in the arguments of the decorated function
                and add more functionalities to it.
            """
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return

            result = function(*args, **kwds)
            return result

        return limited_function

    return callLimiter  # return the decorator
