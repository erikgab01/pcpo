from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.viewsets import ModelViewSet

from goodweather.models import GoodDay


class HomePageListView(ListView):
	model = GoodDay
	template_name = 'goodweather/homepage.html'