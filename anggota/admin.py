# In your admin.py file of your Django app

from django.contrib import admin
from .models import Member, Absen

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('pan_number', 'name', 'status_member')
    search_fields = ('pan_number', 'name')
    list_filter = ('status_member',)

@admin.register(Absen)
class AbsenAdmin(admin.ModelAdmin):
    list_display = ('member', 'amal', 'jam_absen')
    search_fields = ('member__pan_number', 'member__name')  # Search based on Member fields
    list_filter = ('amal', 'jam_absen', 'member__status_member')  # Filter based on Absen and Member fields
