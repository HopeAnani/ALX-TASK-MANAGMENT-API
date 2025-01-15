from django.urls import path
from . import views
from .views import TaskListCreateAPIView

app_name = 'task'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('add/', views.add_task, name='add'),
    path('<uuid:pk>/', views.task, name= 'task'),
    path('<uuid:pk>/edit/', views.edit_task, name= 'edit'),
    path('<uuid:pk>/delete/', views.delete_task, name= 'delete'),
    path('<uuid:pk>/complete/', views.complete_task, name='complete'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
]