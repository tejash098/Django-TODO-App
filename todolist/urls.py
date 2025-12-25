from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo_detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('todo_create/', views.todo_create, name='todo_create'),
    path('todo_update/<int:todo_id>/', views.todo_update, name='todo_update'),
    path('todo_delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
]