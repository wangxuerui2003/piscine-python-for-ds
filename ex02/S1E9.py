from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract character class"""

    def __init__(self, first_name, is_alive=True):
        """Character class constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's is_alive to False"""
        pass


class Stark(Character):
    """Stark class inherited from Character class"""

    def __init__(self, first_name, is_alive=True):
        """Stark class constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Set the stark's is_alive to False"""
        self.is_alive = False
