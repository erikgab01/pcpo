from .connector import StoreConnector
from pandas import DataFrame, Series
from datetime import datetime

# Вывод списка запросов
def select_all_from_source_files(connector: StoreConnector):
    connector.start_transaction()  # начинаем выполнение запросов
    query = f'SELECT * FROM queries'
    result = connector.execute(query).fetchall()
    connector.end_transaction()  # завершаем выполнение запросов
    return result

# Вставка в таблицу queries
def insert_into_source_files(connector: StoreConnector, filename: str):
    now = datetime.now() # текущая дата и время
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")   # преобразуем в формат SQL
    connector.start_transaction()
    query = f'INSERT INTO queries (processed) VALUES (\'{date_time}\')'
    result = connector.execute(query)
    connector.end_transaction()
    return result

# Вставка данных goodday
def insert_rows_into_processed_data(connector: StoreConnector, dataframe, filename: str):
    rows = dataframe
    connector.start_transaction()
    
    for row in rows:
        date_ms = datetime.strptime(row['dt'], '%B %d, %Y').timestamp()
        connector.execute(f'INSERT INTO goodweather_goodday (date1, weather, date_millisecs, query1) VALUES (\'{row["dt"]}\', \'{row["weather_main"]}\', \'{date_ms}\', 1)')
    connector.end_transaction()