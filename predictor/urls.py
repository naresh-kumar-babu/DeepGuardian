from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('inspect/', inspect, name='inspect'),
    path('about/', about, name='about')
]
