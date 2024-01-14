# yourappname/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('absen', absen_page, name='absen'),
    path('absen/<pan>', absen, name='absen_hit'),
    path('absen2/<pan>', absen2, name='absen_hit2'),
    path('absen3', absen3, name='absen_hit2'),
    path('', data_anggota, name='anggota'),
    path('data-absen', data_absen, name='data_absen'),

    path('tambah-anggota', tambah_anggota, name='tambah_anggota'),
    path('delete-anggota/<pk>', delete_anggota, name='delete_anggota'),







]
