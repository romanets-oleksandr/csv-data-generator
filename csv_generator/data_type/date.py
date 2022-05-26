import random
import time
from datetime import datetime

from .base import DataTypeGenerator


class DateGenerator(DataTypeGenerator):
    def generate_value(self):
        d = random.randint(1, int(time.time()))
        return datetime.fromtimestamp(d).strftime('%Y-%m-%d')
