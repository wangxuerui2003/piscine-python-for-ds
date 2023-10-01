def callLimit(limit: int):
    """
        A function that returns a decorator
        which limits the number of calls the decorated function can make
        by passing in the "limit" argument
    """
    count = 0

    def callLimiter(function):
        """The decorator function"""
        def limited_function(*args: any, **kwds: any):
            """
                Inner function of the decorator
                which takes in the arguments of the decorated function
                and add the calls limitation to it.
            """
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return

            result = function(*args, **kwds)
            return result

        return limited_function  # return the wrapper function

    return callLimiter  # return the decorator
