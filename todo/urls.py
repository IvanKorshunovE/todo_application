from django.urls import path

from todo.views import (
    TaskListView,
    ToggleAssignToTaskView,
    TaskDeleteView,
    TaskUpdateView,
    CreateTaskView,
    TagsListView,
    CreateTagView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", CreateTaskView.as_view(), name="task-create"),
    path("tasks/<int:pk>/complete/", ToggleAssignToTaskView.as_view(), name="toggle-complete"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", CreateTagView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
