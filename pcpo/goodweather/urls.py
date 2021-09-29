from django.urls import path, include

from goodweather.views import HomePageListView

urlpatterns = [
    path('home/', HomePageListView.as_view(), name='home'),
]
