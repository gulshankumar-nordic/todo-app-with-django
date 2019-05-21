from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addItem, name="add"),
    path('completed/<todoId>', views.completedItem, name="completed"),
    path('uncheckcompleted/<todoId>', views.uncheckCompleted, name="uncheckcompleted"),
    path('deletecompleted/', views.deleteCompleted, name="deletecompleted"),    
    path('deleteall/', views.deleteAll, name="deleteall"),    

]