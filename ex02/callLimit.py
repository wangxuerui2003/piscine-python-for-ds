def callLimit(limit: int):
    """A decorator to limit the number of calls of a function"""
    count = 0

    def callLimiter(function):
        """middle function of the decorator"""
        def limited_function(*args: any, **kwds: any):
            """inner function of the decorator"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return

            result = function(*args, **kwds)
            return result

        return limited_function

    return callLimiter
