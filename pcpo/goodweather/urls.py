from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

from goodweather.views import Day7ListView, HistoryListView, welcome

urlpatterns = [
    path('', RedirectView.as_view(url='/welcome/', permanent=False)),
    path('home/<int:day>/', Day7ListView.as_view(), name='home'),
    path('history/', HistoryListView.as_view(), name='history'),
    path('welcome/', welcome, name='welcome'),
]
