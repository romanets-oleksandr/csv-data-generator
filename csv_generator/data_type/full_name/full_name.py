import random
from pathlib import Path
from ..base import DataType

_cd = Path(__file__).parent
FIRST_NAMES_PATH = _cd / 'first-names.txt'
LAST_NAMES_PATH = _cd / 'last-names.txt'


class FullName(DataType):
    def __init__(self):
        with open(FIRST_NAMES_PATH) as f:
            self.first_names = f.readlines()

        with open(LAST_NAMES_PATH) as f:
            self.last_names = f.readlines()

    def generate_value(self):
        return f'{random.choice(self.first_names)} {random.choice(self.last_names)}'
