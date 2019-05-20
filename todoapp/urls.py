from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addItem, name="add"),
    path('completed/<todoId>', views.completedItem, name="completed"),
    
]