import random

from .base import DataTypeGenerator


class IntegerGenerator(DataTypeGenerator):
    def generate_value(self):
        _min = self.column.min_range or 0
        _max = self.column.max_range or 100
        return random.randint(_min, _max)
