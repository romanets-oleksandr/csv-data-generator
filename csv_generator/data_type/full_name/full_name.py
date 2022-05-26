import random
from pathlib import Path
from ..base import DataTypeGenerator

_cd = Path(__file__).parent
FIRST_NAMES_PATH = _cd / 'first-names.txt'
LAST_NAMES_PATH = _cd / 'last-names.txt'


class FullNameGenerator(DataTypeGenerator):
    def __init__(self, column):
        super().__init__(column)

        with open(FIRST_NAMES_PATH) as f:
            self.first_names = f.readlines()

        with open(LAST_NAMES_PATH) as f:
            self.last_names = f.readlines()

    def generate_value(self):
        name = random.choice(self.first_names).strip()
        last_name = random.choice(self.last_names).strip()
        return f'{name} {last_name}'
