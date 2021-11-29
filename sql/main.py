from processor.dataprocessorfactory import *    # подключаем фабрику обработчиков данных
from repository.connectorfactory import *       # подключаем фабрику коннекторов к БД
from repository.sql_api import *                # подключаем API для работы с БД
import time

"""
    Данный модуль запускает программу
        ("точка входа" приложения)
"""
DATASOURCE = "https://api.openweathermap.org/data/2.5/onecall"
DB_URL = 'sqlite:///newdb.db'

# В зависимости от расширения файла вызываем соответствующий фабричный метод
def init_processor(source: str) -> DataProcessor:
    proc = None
    if source.endswith('.csv'):
        proc = CsvDataProcessorFactory().get_processor(source)
    elif source.endswith('.txt'):
        proc = TxtDataProcessorFactory().get_processor(source)
    else:
        proc = ApiDataProcessorFactory().get_processor(source)
    return proc

# Запуск обработки
def run_processor(proc: DataProcessor) -> DataFrame:
    proc.run()
    proc.print_result()
    return proc.result


if __name__ == '__main__':
    result = None   # результат обработки данных
    # Запуск обработчика данных
    proc = init_processor(DATASOURCE)
    if proc is not None:
        result = run_processor(proc)

    # Работа с БД
    if result is not None:
        print(result)
        db_connector = SQLStoreConnectorFactory().get_connector(DB_URL)   # получаем объект соединения
        insert_into_source_files(db_connector, DATASOURCE)                # сохраняем в БД информацию о файле с набором данных
        print(select_all_from_source_files(db_connector))                 # вывод списка всеъ обработанных файлов
        insert_rows_into_processed_data(db_connector, result, DATASOURCE)     # записываем в БД 5 первых строк результата
        # Завершаем работу с БД
        db_connector.close()
