from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from pyexpat import model

from tasker.forms import *

from tasker.models import Worker, TaskType, Task, Position, Team, Project


@login_required
def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    num_positions = Position.objects.count()
    num_teams = Team.objects.count()
    num_projects = Project.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_task_types": num_task_types,
        "num_positions": num_positions,
        "num_teams": num_teams,
        "num_projects": num_projects,
        "num_visits": num_visits,
    }

    return render(request, "tasker/index.html", context=context)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 3
    queryset = Position.objects.all().select_related("workers")

    def get_context_data(self, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        position = self.request.GET.get("name", "")
        context["position"] = position
        context["search_form"] = PositionSearchForm(
            {"model": model, "position": position}
        )
        return context

    def get_queryset(self):
        queryset = Position.objects.select_related()
        form = PositionForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasker:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasker:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasker:position-list")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasker:worker-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.prefetch_related("teams")

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["username"] = username
        context["search_form"] = WorkerSearchForm(
            {"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasker:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("tasker:worker-list")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("tasker:tasktype-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 3
    queryset = TaskType.objects.prefetch_related("tasks")

    def get_context_data(self, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TaskTypeSearchForm(
            {"model": model, "name": name}
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.select_related()
        form = TaskTypeForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("tasker:tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasker:tasktype-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasker:task-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 3
    queryset = Task.objects.prefetch_related("workers")

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TaskSearchForm(
            {"model": model, "name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.select_related()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasker:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasker:task-list")


class WorkerPositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerPositionUpdateForm
    success_url = reverse_lazy("tasker:worker-list")


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasker:team-list")


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TeamSearchForm(
            {"model": model, "name": name}
        )
        return context

    def get_queryset(self):
        queryset = Team.objects.select_related()
        form = TeamSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasker:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("tasker:team-list")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasker:project-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = ProjectSearchForm(
            {"model": model, "name": name}
        )
        return context

    def get_queryset(self):
        queryset = Project.objects.select_related()
        form = ProjectSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasker:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasker:project-list")


def projects_toggle_done(request, pk):
    project = Project.objects.get(id=pk)
    project.is_completed = not project.is_completed
    project.save()
    return HttpResponseRedirect(reverse_lazy("tasker:project-list"))


class TaskToggleDoneView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        success_url = reverse_lazy("tasker:task-list")
        return redirect(success_url)


class TeamToggleDoneView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        team = get_object_or_404(Team, pk=pk)
        team.is_active = not team.is_active
        team.save()
        success_url = reverse_lazy("tasker:team-list")
        return redirect(success_url)


class ProjectToggleDoneView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        project = get_object_or_404(Project, pk=pk)
        project.is_completed = not project.is_completed
        project.save()
        success_url = reverse_lazy("tasker:project-list")
        return redirect(success_url)
