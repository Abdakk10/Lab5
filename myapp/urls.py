# myapp/urls.py
from django.urls import path
from .views import add, show_all

urlpatterns = [
    path('add/', add, name='add'),
    path('show_all/', show_all, name='show_all'),
]
