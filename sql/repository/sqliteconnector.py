from .connector import StoreConnector
import sqlite3

# Реализация коннектора для БД SQLite
class SQLiteStoreConnector(StoreConnector):
    def __init__(self, datastore):
        StoreConnector.__init__(self, datastore)
        self._cursor = None

    def connect(self):
        try:
            # Подключаемся к файлу по указанному пути без префикса 'sqlite:///'
            connection = sqlite3.connect(self._datastore[10:])
            cursor = connection.cursor()
            # Включаем поддержку внешних ключей для SQLite
            cursor.execute("PRAGMA foreign_keys = 1")
            cursor.close()
            self.connection = connection
            print("SQLite database connected.")
            return True
        except Exception as e:
            print(f'Connection error: {str(e)}')
            return False

    def execute(self, query):
        result = None
        if self._cursor is not None:
            try:
                result = self._cursor.execute(query)
            except Exception as e:
                self.connection.rollback()
                print(f'Query execution error: {str(e)}')
        else:
            print("Use start_transaction() first.")
        return result

    def start_transaction(self):
        if self._cursor is None and self.connection is not None:
            self._cursor = self.connection.cursor()

    def end_transaction(self):
        if self.connection is not None and self._cursor is not None:
            self.connection.commit()
            self._cursor.close()
            self._cursor = None

    def close(self):
        self.connection.close()
        self.connection = None
