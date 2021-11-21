import requests
from datetime import datetime

from django.core.management.base import BaseCommand
from goodweather.models import GoodDay


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = self.get_data()
        days = self.optimize_data(data)

        for day_num in days:
            # If the day passes according to the criteria, then it is saved in the database
            if self.check_is_good(days[day_num]):
                self.save_day(day_num, days[day_num])

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

    def optimize_data(self, data):
        days = dict(zip(range(8), data))
        for day in days:
            # Current day
            current_day = days[day]
            # Optimize the dictionary view
            # current_day['temp_min'] = current_day['temp']['min']
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

    def check_is_good(self, day):
        return (day['temp_min'] >= -20) and (day['temp_max'] <= 5) \
               and (day['feels_like_day'] >= -20) and (day['feels_like_day'] <= 5) \
               and (day['pressure'] >= 980) and (day['pressure'] <= 1036) \
               and (day['humidity'] >= 40) and (day['humidity'] <= 90) \
               and (day['dew_point'] <= 55) and (day['wind_speed'] <= 14) \
               and (day['uvi'] <= 2) and (day['pop'] <= 50) and 'rain' not in day

    def save_day(self, day_num, day):
        # Saving data into model objects
        day_time = day['dt']
        # If day wasn't saved before
        if not GoodDay.objects.filter(date=day_time).exists():
            good_day = GoodDay()
            good_day.date = day_time
            good_day.temp_min = day['temp_min']
            good_day.temp_min = day['temp_max']
            good_day.feels_like_day = day['feels_like_day']
            good_day.pressure = day['pressure']
            good_day.humidity = day['humidity']
            good_day.dew_point = day['dew_point']
            good_day.wind_speed = day['wind_speed']
            good_day.uvi = day['uvi']
            good_day.pop = day['pop']
            good_day.weather = day['weather_desc']
            good_day.save()
            print(f"Saved {day_num}")
        else:
            print("not saved")

        return True
