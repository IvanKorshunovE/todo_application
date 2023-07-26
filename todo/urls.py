from django.urls import path

from todo.views import TaskView

urlpatterns = [
    path("", TaskView.as_view()),
]

app_name = "todo"
