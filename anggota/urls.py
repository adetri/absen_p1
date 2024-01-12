# yourappname/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('absen', absen_page, name='absen'),

]
