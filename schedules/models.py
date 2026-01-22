# schedules/models.py
from django.db import models
from django.contrib.auth.models import User

class Shift(models.Model):
    # 誰のシフトか（Django標準のユーザーモデルと紐付け）
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    # 日付
    date = models.DateField()
    # 開始時間
    start_time = models.TimeField()
    # 終了時間
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.date} - {self.staff.username}"