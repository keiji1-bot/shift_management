from django.urls import path
from .views import ShiftListView, ShiftCreateView

urlpatterns = [
    path('', ShiftListView.as_view(), name='shift_list'),
    path('create/', ShiftCreateView.as_view(), name='shift_create'),
]