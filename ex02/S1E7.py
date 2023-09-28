from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        """Baratheon class constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Set the baratheon's is_alive to False"""
        self.is_alive = False

    def __str__(self):
        '''An informal string representation of Baratheon objects'''
        return (f'Character {self.family_name} with'
                f' {self.eyes} eyes and {self.hairs} hairs')

    def __repr__(self):
        '''A formal string representation of Baratheon objects'''
        class_name = type(self).__name__
        return f"Vector: ('{class_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        """Lannister class constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Set the lannister's is_alive to False"""
        self.is_alive = False

    def __str__(self):
        '''An informal string representation of Lannister objects'''
        return (f'Character {self.family_name} with'
                f' {self.eyes} eyes and {self.hairs} hairs')

    def __repr__(self):
        '''A formal string representation of Lannister objects'''
        class_name = type(self).__name__
        return f"Vector: ('{class_name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool):
        '''Create a new Lannister object with the arguments passed in'''
        return Lannister(first_name, is_alive)
