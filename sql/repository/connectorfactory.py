from abc import ABC, abstractmethod
from .connector import StoreConnector
from .mysqlconnector import MySQLStoreConnector
from .sqliteconnector import SQLiteStoreConnector

"""
    В данном модуле реализуется фабрика для коннекторов к хранилищу данных
"""

class StoreConnectorFactory(ABC):
    def __init__(self):
        self.instance = None

    @abstractmethod
    def get_connector(self, datastore) -> StoreConnector:
        pass

"""
    Пример реализации параметризированного фабричного метода
    для получения объектов соединения с различными SQL БД 
    (в зависимости от формата строки подключения).
    
    Допустимые форматы строк подключения:
    
    SQLite: "sqlite:///test.db" (файл БД в локальной папке приложения)
            "sqlite:///C:\\databases\\test.db" (полный путь до файла БД)
            
    MySQL: "pymysql://usr:qwerty@192.168.56.104/testdb"
    
    Параметризированный фабричный метод может применяться, когда 
    создание того или иного объекта определяется одним параметром.
"""

class SQLStoreConnectorFactory(StoreConnectorFactory):
    def get_connector(self, datastore):
        if datastore.startswith("sqlite:///"):
            self.instance = SQLiteStoreConnector(datastore)
            if self.instance.connect():
                return self.instance
        elif datastore.startswith("pymysql://"):
            self.instance = MySQLStoreConnector(datastore)
            if self.instance.connect():
                return self.instance
        return None