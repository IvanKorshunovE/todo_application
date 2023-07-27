from django.urls import path

from todo.views import (
    TaskView,
    TaskDetailView,
    TaskDeleteView
)

urlpatterns = [
    path("tasks/", TaskView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete")
]

app_name = "todo"
