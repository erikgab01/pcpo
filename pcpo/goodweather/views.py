from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView

from goodweather.models import GoodDay


class HomePageListView(ListView):
	model = GoodDay
	template_name = 'goodweather/homepage.html'


class CustomLoginView(LoginView):
    template_name = "goodweather/login.html"


class CustomLogoutView(LogoutView):
    next_page = '/login/'