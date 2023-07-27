from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView, DeleteView
)

from todo.models import Task


class TaskView(ListView):
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 10


class TaskDetailView(DetailView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
