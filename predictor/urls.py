from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('verify/', verify, name='verify'),
    path('results/<face>/', results, name='results'),
    path('about/', about, name='about')
]
