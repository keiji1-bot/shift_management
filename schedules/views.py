from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Shift

class ShiftListView(ListView):
    model = Shift
    template_name = 'schedules/shift_list.html'
    context_object_name = 'shifts'
    ordering = ['date']

# 新しい機能（追加画面）の仕組み
class ShiftCreateView(CreateView):
    model = Shift
    # ★修正箇所：ここを 'person_name' から 'staff' に変更しました
    fields = ['staff', 'date', 'start_time', 'end_time']
    template_name = 'schedules/shift_form.html'
    success_url = reverse_lazy('shift_list')