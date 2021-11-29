from .connector import StoreConnector
import pymysql

# Реализация коннектора для БД MySQL
class MySQLStoreConnector(StoreConnector):
    def __init__(self, datastore):
        # Удаляем префикс 'pymysql://'
        self._datastore = datastore[10:]
        # Разбираем строку подключения через функцию split()
        con_str_list = self._datastore.split(':')
        self._user = con_str_list[0]
        con_str_list = con_str_list[1].split('@')
        self._password = con_str_list[0]
        con_str_list = con_str_list[1].split('/')
        self._host = con_str_list[0]
        self._db = con_str_list[1]
        self._cursor = None

    def connect(self):
        try:
            self.connection = pymysql.connect(host=self._host,
                                              user=self._user,
                                              password=self._password,
                                              db=self._db,
                                              charset='utf8mb4')
            print("MySQL database connected.")
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
