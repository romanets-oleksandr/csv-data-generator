from .base import DataTypeGenerator
from .full_name import FullNameGenerator
from .job import JobGenerator
from .date import DateGenerator
from .integer import IntegerGenerator
from .email import EmailGenerator


_types = {
    'Full name': FullNameGenerator,
    'Job': JobGenerator,
    'Date': DateGenerator,
    'Integer': IntegerGenerator,
    'Email': EmailGenerator
}


def get_generator(column) -> DataTypeGenerator:
    return _types[column.data_type](column)


def get_choices() -> list[tuple]:
    return [(k, k) for k in _types.keys()]
