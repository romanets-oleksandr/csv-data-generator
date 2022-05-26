import random
from pathlib import Path
from ..base import DataTypeGenerator

_cd = Path(__file__).parent
JOBS_PATH = _cd / 'jobs.txt'


class JobGenerator(DataTypeGenerator):
    def __init__(self, column):
        super().__init__(column)
        with open(JOBS_PATH) as f:
            self.jobs = f.readlines()

    def generate_value(self):
        return random.choice(self.jobs).strip()
