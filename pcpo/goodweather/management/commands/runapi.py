import requests

from django.core.management.base import BaseCommand
from goodweather.models import GoodDay


class Command(BaseCommand):
	def handle(self, *args, **options):
		app_id = "27e3431f680b5d8be99fbbeed12e2dde"
		# Coordinates (Ufa)
		lat = 54.775
		lon = 56.0375
		# To get rid of extra data
		exclude = "current,minutely,hourly"
		# To get temperature in Celcius
		units = 'metric'
		# Additional args
		city_id = 479561 	# Ufa
		mode = 'json'	# Specifies output file
		city = "Ufa,RU"
		# Making request
		try:
			# This'll return weather forecast for 7 days ahead
			res2 = requests.get(
				"https://api.openweathermap.org/data/2.5/onecall",
				params={'lat': lat, 'lon': lon, 'appid': app_id, 'exclude': exclude, 'units': units}
			)
			data = res2.json()
			# Saving data into model objects
			for number, day in enumerate(data['daily']):
				day_time = str(day['dt'])
				# If day wasn't saved before
				if not GoodDay.objects.filter(date=day_time).exists():
					good_day = GoodDay()
					good_day.temp = day['temp']['day']
					good_day.temp_feels_like = day['feels_like']['day']
					good_day.humidity = day['humidity']
					good_day.pressure = day['pressure']
					good_day.wind_speed = day['wind_speed']
					good_day.weather = day['weather'][0]['main']
					good_day.date = day_time
					good_day.save()
					print(f"Saved {number}")
				else:
					print("not saved")
		except Exception as e:
			print("Exception: ", e)
			pass
