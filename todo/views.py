from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskCreateForm, TaskUpdateForm
from todo.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_tasks": Task.objects.count(),
        "num_tags": Tag.objects.count(),
        "completed_tasks": Task.objects.filter(status=True).count(),
    }
    return render(
        request,
        "todo/index.html",
        context=context)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3
    ordering = ['status', '-create']


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def compete_undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse_lazy('todo:task-list'))


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 7
    ordering = ["name"]


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
