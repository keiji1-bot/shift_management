# schedules/urls.py
from django.urls import path
from .views import ShiftListView, ShiftCreateView

urlpatterns = [
    path('', ShiftListView.as_view(), name='shift_list'),
    path('add/', ShiftCreateView.as_view(), name='shift_add'),
]