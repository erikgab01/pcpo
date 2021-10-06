from django.db import models


class GoodDay(models.Model):
	date = models.CharField(max_length=40, verbose_name='date', null=True, blank=True)
	weather = models.CharField(max_length=20, verbose_name='weather', null=True, blank=True)

	temp_min = models.FloatField(verbose_name='temp_min', null=True, blank=True)
	temp_max = models.FloatField(verbose_name='temp_max', null=True, blank=True)
	feels_like_day = models.FloatField(verbose_name='feels_like_day', null=True, blank=True)
	pressure = models.IntegerField(verbose_name='pressure', null=True, blank=True)
	humidity = models.IntegerField(verbose_name='humidity', null=True, blank=True)
	dew_point = models.FloatField(verbose_name='dew_point', null=True, blank=True)
	wind_speed = models.FloatField(verbose_name='wind_speed', null=True, blank=True)
	uvi = models.FloatField(verbose_name='uvi', null=True, blank=True)
	pop = models.IntegerField(verbose_name='pop', null=True, blank=True)
	
	def __str__(self):
		return self.weather


	class Meta:
		verbose_name_plural = 'GoodDays'
		verbose_name = 'GoodDay'
		ordering = ['-date']