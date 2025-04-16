from django.urls import path

from .models import Worker, TaskType
from .views import (
    index,
    PositionCreateView,
    PositionDeleteView,
    PositionListView,
    PositionUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
    TaskTypeCreateView,
    TaskTypeDeleteView,
    TaskTypeListView,
    TaskTypeUpdateView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerDetailView,
    WorkerListView,
    WorkerUpdateView,
)
urlpatterns = [
    path("", index, name="index"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(), name="tasktype-create"),

    path("tasktypes/", TaskTypeListView.as_view(), name="tasktype-list"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="tasktype-update"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="tasktype-delete"),





]

app_name = "tasker"