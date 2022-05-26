from .base import DataType
from .full_name import FullName


_types = {
    'Full name': FullName
}


def get_data_type(name: str) -> DataType:
    return _types[name]


def get_choices() -> list[tuple]:
    return [(k, k) for k in _types.keys()]
