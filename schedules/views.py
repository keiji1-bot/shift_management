from django.shortcuts import render

# Create your views here.
# schedules/views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Shift

# シフト一覧を表示するビュー
class ShiftListView(ListView):
    model = Shift
    template_name = 'schedules/shift_list.html'
    ordering = ['date'] # 日付順に並べる

# シフトを登録するビュー
class ShiftCreateView(CreateView):
    model = Shift
    template_name = 'schedules/shift_form.html'
    fields = ['staff', 'date', 'start_time', 'end_time']
    success_url = reverse_lazy('shift_list') # 成功したら一覧に戻る