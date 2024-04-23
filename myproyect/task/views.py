
from django.shortcuts import get_object_or_404, render
from .models import Task


def index(request):
    latest_task_list = Task.objects.order_by("-fecha_realizar")[:5]
    context = {"latest_task_list": latest_task_list}
    return render(request, "task/index.html", context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "task/detail.html", {"task": task})
