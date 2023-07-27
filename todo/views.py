from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(ListView):
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = True
        return context


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDetailView(DetailView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class ToggleAssignToTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:task-list")


class TagsListView(ListView):
    queryset = Tag.objects.all()
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = True
        return context


class CreateTagView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags-list")
