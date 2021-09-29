from django.db import models


class GoodDay(models.Model):
	prop1 = models.CharField(max_length=20, verbose_name='prop1')
	prop2 = models.CharField(max_length=20, verbose_name='prop2', null=True, blank=True)
	prop3 = models.CharField(max_length=20, verbose_name='prop3', null=True, blank=True)
	
	def __str__(self):
		return self.prop1


	class Meta:
		verbose_name_plural = 'GoodDays'
		verbose_name = 'GoodDay'
		ordering = ['-prop1']