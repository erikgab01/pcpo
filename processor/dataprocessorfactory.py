from abc import ABC, abstractmethod
from .dataprocessor import *

"""
    В данном модуле объявляются классы, реализующие фабричный метод get_processor, 
    который возвращает соответствующие классы обработчиков данных
"""


class DataProcessorFactory(ABC):
    @abstractmethod
    def get_processor(self, datasource) -> DataProcessor:
        pass


"""
    Фабричный метод может не только возвращать класс соответствующего обработчика,
    здесь также может быть реализована логика, которая меняет поведение данного обработчика,
    например, меняет тип разделителя и кодировку для CSV-файла (через атрибуты класса),
    применяет различные режимы обработки и т.д.
"""


class CsvDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, datasource) -> DataProcessor:
        return CsvDataProcessor(datasource)


class TxtDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, datasource) -> DataProcessor:
        return TxtDataProcessor(datasource)


class ApiDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, datasource) -> DataProcessor:
        return ApiDataProcessor(datasource)
