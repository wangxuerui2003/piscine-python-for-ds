from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The King class"""
    def __init__(self, first_name: str, is_alive=True):
        """King class constructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """setter to set new eyes property"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """setter to set new hairs property"""
        self.hairs = hairs

    def get_eyes(self):
        """get the eyes property"""
        return self.eyes

    def get_hairs(self):
        """get the hairs property"""
        return self.hairs
