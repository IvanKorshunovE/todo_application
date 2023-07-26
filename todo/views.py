from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task


class TaskView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    # template_name = 'home.html'
    # context_object_name = 'books'
    paginate_by = 2

    # def get_queryset(self, *args, **kwargs):
    #     return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))
