from django.urls import path

from .views import TodoCreateView, TodoUpdateView, TodoDeleteView, TodoDetailView, TodoListView, task_done


app_name = 'todo'
urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/set-done/', task_done, name='done'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
    path('create/', TodoCreateView.as_view(), name='create'),
]