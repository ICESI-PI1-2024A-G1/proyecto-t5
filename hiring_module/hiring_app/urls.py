from django.urls import path
from .views import home

app_name = 'hiring_app'

urlpatterns = [
    path('home/', home, name = 'home',)
]