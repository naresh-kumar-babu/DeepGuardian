from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('inspect/', verify, name='inspect'),
    path('about/', about, name='about')
]
