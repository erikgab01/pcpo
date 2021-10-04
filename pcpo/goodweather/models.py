from django.db import models


class GoodDay(models.Model):
	temp = models.FloatField(verbose_name='temp')
	temp_feels_like = models.FloatField(verbose_name='temp_feels_like', null=True, blank=True)
	humidity = models.IntegerField(verbose_name='humidity', null=True, blank=True)
	pressure = models.IntegerField(verbose_name='pressure', null=True, blank=True)
	wind_speed = models.FloatField(verbose_name='wind_speed', null=True, blank=True)
	weather = models.CharField(max_length=20, verbose_name='weather', null=True, blank=True)
	date = models.CharField(max_length=40, null=True, blank=True)
	
	def __str__(self):
		return self.weather


	class Meta:
		verbose_name_plural = 'GoodDays'
		verbose_name = 'GoodDay'
		ordering = ['-temp']