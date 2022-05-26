import random
import string

from .base import DataTypeGenerator


MAIL_DOMAINS = ('gmail.com', 'yahoo.com', 'hotmail.com', 'live.com', 'outlook.com')


class EmailGenerator(DataTypeGenerator):
    def generate_value(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
        return f'{name}@{random.choice(MAIL_DOMAINS)}'
