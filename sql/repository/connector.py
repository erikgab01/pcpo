from abc import ABC, abstractmethod     # подключаем инструменты для создания абстрактных классов

"""
    В данном модуле реализуются классы, определяющие подключения к
    различным базам данных (БД).
    
    ВАЖНО! Если реализация классов-потомков занимает большое 
    количество строк, то необходимо оформлять каждый класс в отдельном файле
"""

# Родительский класс для коннекторов БД
class StoreConnector(ABC):
    def __init__(self, datastore):
        # общие атрибуты
        self._datastore = datastore   # путь к хранилищу данных (БД)
        self.connection = None       # объект

    # Метод, инициализирующий соединение с БД
    # Все методы, помеченные декоратором @abstractmethod, ОБЯЗАТЕЛЬНЫ для переобределения
    @abstractmethod
    def connect(self) -> bool:
        pass

    # Выполнение запроса
    @abstractmethod
    def execute(self, query: str):
        pass

    # Метод, подготавливающий коннектор к выполнению запросов в БД
    @abstractmethod
    def start_transaction(self):
        pass

    # Метод, завершающий выполнение запросов в БД
    @abstractmethod
    def end_transaction(self):
        pass

    # Завершение соединения с БД
    @abstractmethod
    def close(self):
        pass

