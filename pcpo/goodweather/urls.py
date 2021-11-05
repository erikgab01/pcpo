from django.urls import path, include

from goodweather.views import HomePageListView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', HomePageListView.as_view()),
    path('home/', HomePageListView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
