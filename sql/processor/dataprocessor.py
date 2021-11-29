from abc import ABC, abstractmethod  # подключаем инструменты для создания абстрактных классов
import pandas  # библиотека для работы с датасетами
import requests
from datetime import datetime

"""
    В данном модуле реализуются классы обработчиков для 
    применения алгоритма обработки к различным типам файлов (csv или txt).
    
    ВАЖНО! Если реализация различных обработчиков занимает большое 
    количество строк, то необходимо оформлять каждый класс в отдельном файле
"""


# Родительский класс для обработчиков файлов
class DataProcessor(ABC):
    def __init__(self, datasource):
        self._datasource = datasource
        self._dataset = None
        self.result = None

    # Метод, инициализирующий источник данных
    # Все методы, помеченные декоратором @abstractmethod, ОБЯЗАТЕЛЬНЫ для переобределения
    @abstractmethod
    def get_data(self):
        pass

    # Точка запуска методов обработки данных
    @abstractmethod
    def run(self):
        pass

    """
        Пример одного из общих методов обработки данных.
        В данном случае метод просто сортирует входной датасет по значению заданной колонки (аргумент col)
        
        ВАЖНО! Следует логически разделять методы обработки, например, отдельный метод для сортировки, 
        отдельный метод для удаления "пустот" в датасете и т.д. Это позволит гибко применять необходимые
        методы при переопределении метода run для того или иного типа обработчика.
        НАПРИМЕР, если ваш источник данных это не файл, а база данных, тогда метод сортировки будет не нужен,
        т.к. сортировку можно сделать при выполнении SQL-запроса типа SELECT ... ORDER BY...

    """

    def check_is_good(self, day):
        return (day['temp_min'] >= -20) and (day['temp_max'] <= 5) \
               and (day['feels_like_day'] >= -20) and (day['feels_like_day'] <= 5) \
               and (day['pressure'] >= 980) and (day['pressure'] <= 1036) \
               and (day['humidity'] >= 40) and (day['humidity'] <= 90) \
               and (day['dew_point'] <= 55) and (day['wind_speed'] <= 14) \
               and (day['uvi'] <= 2) and (day['pop'] <= 50) and 'rain' not in day

    def optimize_data(self, data):
        days = dict(zip(range(8), data))
        for day in days:
            # Current day
            current_day = days[day]
            # Optimize the dictionary view
            current_day['temp_min'] = current_day['temp']['min']
            current_day['temp_max'] = current_day['temp']['max']
            current_day['feels_like_day'] = current_day['feels_like']['day']
            current_day['weather_main'] = current_day['weather'][0]['main']
            current_day['weather_desc'] = current_day['weather'][0]['description']
            # Delete unimportant information
            del current_day['sunrise'], \
                current_day['sunset'], \
                current_day['moonrise'], \
                current_day['moonset'], \
                current_day['moon_phase'], \
                current_day['clouds'], \
                current_day['wind_deg'], \
                current_day['wind_gust'], \
                current_day['temp'], \
                current_day['feels_like'], \
                current_day['weather']
            # Transform seconds to Date in correct format
            current_day['dt'] = datetime.fromtimestamp(current_day['dt']).strftime('%B %d, %Y')
            print(f'Day {day}: {days[day]}')
        return days

    # Абстрактный метод для вывоа результата на экран
    @abstractmethod
    def print_result(self):
        pass


# Реализация класса-обработчика csv-файлов
class CsvDataProcessor(DataProcessor):
    """
        Переопределяем метод инициализации источника данных.
        Т.к. данный класс предназначен для чтения CSV-файлов, то используем метод read_csv
        из библиотеки pandas
    """

    def get_data(self):
        self._dataset = pandas.read_csv(self._datasource, sep=';', header='infer', names=None, encoding="utf-8")
        return self._dataset

    #    Сортируем данные по значениям колонки "LKG" и сохраняем результат в атрибуте result
    def run(self):
        data = self.get_data()
        days = self.optimize_data(data)
        self.result = []
        for day_num in days:
            # If the day passes according to the criteria, then it is saved in the database
            if self.check_is_good(days[day_num]):
                self.result.append(day_num)
        self.print_result()

    def print_result(self):
        print(f'Running CSV-file processor!\n', self.result)


# Реализация класса-обработчика txt-файлов
class TxtDataProcessor(DataProcessor):
    # Реализация метода для чтения TXT-файла
    def get_data(self):
        self._dataset = pandas.read_table(self._datasource, sep='\s+', engine='python')
        return self._dataset

    def run(self):
        data = self.get_data()
        days = self.optimize_data(data)
        self.result = []
        for day_num in days:
            # If the day passes according to the criteria, then it is saved in the database
            if self.check_is_good(days[day_num]):
                self.result.append(day_num)
        self.print_result()

    def print_result(self):
        print(f'Running TXT-file processor!\n', self.result)


# Реализация класса-обработчика api-запросов
class ApiDataProcessor(DataProcessor):
    # Реализация метода для api-запроса
    def get_data(self):
        app_id = "27e3431f680b5d8be99fbbeed12e2dde"
        # Coordinates (Ufa)
        lat = 54.775
        lon = 56.0375
        # To get rid of extra data
        exclude = "current,minutely,hourly"
        # To get temperature in Celcius
        units = 'metric'
        data = None
        # Making request
        try:
            # This'll return weather forecast for 7 days ahead
            res2 = requests.get(
                "https://api.openweathermap.org/data/2.5/onecall",
                params={'lat': lat, 'lon': lon, 'appid': app_id, 'exclude': exclude, 'units': units}
            )
            data = res2.json()
        except Exception as e:
            print("Exception: ", e)
            pass

        return data['daily']

    def run(self):
        data = self.get_data()
        days = self.optimize_data(data)
        self.result = []
        for day_num in days:
            # If the day passes according to the criteria, then it is saved in the database
            if self.check_is_good(days[day_num]):
                self.result.append(days[day_num])
        self.print_result()

    def print_result(self):
        print(f'Running API-file processor!\n', self.result)
