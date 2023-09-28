class calculator:
    """the calculator class (static)"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]):
        dp = sum(a * b for a, b in zip(V1, V2))
        print("Dot product is", dp)
        return dp

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]):
        vec = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", vec)
        return vec

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]):
        vec = [float(a - b) for a, b in zip(V1, V2)]
        print("Add Vector is :", vec)
        return vec
