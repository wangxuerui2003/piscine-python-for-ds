class calculator:
    """the calculator class"""
    def __init__(self, numbers: list[float]):
        """the calculator class constructor"""
        self.numbers = numbers

    def __add__(self, object):
        """+ operator"""
        self.numbers = [num + object for num in self.numbers]
        print(self.numbers)
        return self.numbers

    def __mul__(self, object):
        """* operator"""
        self.numbers = [num * object for num in self.numbers]
        print(self.numbers)
        return self.numbers

    def __sub__(self, object):
        """- operator"""
        self.numbers = [num - object for num in self.numbers]
        print(self.numbers)
        return self.numbers

    def __truediv__(self, object):
        """/ operator"""
        if object == 0:
            print("division by zero!")
            return self.numbers

        self.numbers = [num / object for num in self.numbers]
        print(self.numbers)
        return self.numbers
