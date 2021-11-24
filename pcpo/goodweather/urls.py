from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

from goodweather.views import Day7ListView, HistoryListView

urlpatterns = [
    path('', RedirectView.as_view(url='/home/7/', permanent=False)),
    path('home/<int:day>/', Day7ListView.as_view(), name='home'),
    path('history/', HistoryListView.as_view(), name='history'),
]
