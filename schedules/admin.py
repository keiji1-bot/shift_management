# schedules/admin.py
from django.contrib import admin
from .models import Shift

# 管理画面で見やすくする設定
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'start_time', 'end_time')

admin.site.register(Shift, ShiftAdmin)