from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('add/', views.add_task, name='add'),
    path('<uuid:pk>/', views.task, name= 'task'),
    path('<uuid:pk>/edit/', views.edit_task, name= 'edit'),
    path('<uuid:pk>/delete/', views.delete_task, name= 'delete'),
    path('<uuid:pk>/complete/', views.complete_task, name='complete'),
    path('api/tasks/', views.TaskListAPIView.as_view(), name='task-list'),
]