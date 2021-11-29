import datetime
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView

from goodweather.models import GoodDay


class Day7ListView(ListView):
    model = GoodDay
    template_name = 'goodweather/7_day.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(date_millisecs__gte=datetime.datetime.now().timestamp()).order_by('date_millisecs')
        return queryset[:self.kwargs['day']]


class HistoryListView(ListView):
    model = GoodDay
    template_name = 'goodweather/history.html'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('date_millisecs')
        return queryset
