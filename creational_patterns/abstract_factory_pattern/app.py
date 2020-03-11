from abc import ABCMeta, abstractmethod
from decimal import Decimal


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def build_sequence(self):
        pass

    @abstractmethod
    def build_number(self, string):
        pass


class Factory(AbstractFactory):
    def build_sequence(self):
        return []

    def build_number(self, string):
        return Decimal(string)


class Loader:
    @staticmethod
    def load(string, factory):
        sequence = factory.build_sequence()
        for substring in string.split(','):
            item = factory.build_number(substring)
            sequence.append(item)
        return sequence


f = Factory()
result = Loader.load('1.23, 4.56', f)
print(result)
