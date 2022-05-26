from abc import ABC, abstractmethod


class DataType(ABC):
    @abstractmethod
    def generate_value(self):
        """Generate data type value"""
