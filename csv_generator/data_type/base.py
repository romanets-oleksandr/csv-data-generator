from abc import ABC, abstractmethod


class DataTypeGenerator(ABC):
    def __init__(self, column):
        self.column = column

    @abstractmethod
    def generate_value(self):
        """Generate data type value"""
