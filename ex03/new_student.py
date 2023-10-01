import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15 ascii lower characters long id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A dataclass that stores the information of a student"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
            Adds custom initialization logic
            after the automatically generated __init__ method has run.
        """
        self.login = self.name[0] + self.surname
        self.id = generate_id()
