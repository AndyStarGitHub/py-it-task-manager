from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):

    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name="workers")
    # REQUIRED_FIELDS = ['position']
    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("tasker:worker-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORIY_CHOICES = {
        "Urgent": "Urgent",
        "High": "High",
        "Low": "Low",
    }

    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORIY_CHOICES.items(), max_length=6, default="Low")
    task_types = models.ManyToManyField(TaskType, related_name="tasks")
    workers = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "deadline"]

    def __str__(self) -> str:
        return self.name


class Team(models.Model):

    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    workers = models.ManyToManyField(Worker, related_name="teams")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-is_active", "name"]

    def __str__(self) -> str:
        return self.name

class Project(models.Model):

    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tasks = models.ManyToManyField(Task, related_name="task_projects")
    teams = models.ManyToManyField(Team, related_name="team_projects")

    class Meta:
        ordering = ["is_completed", "deadline"]

    def __str__(self) -> str:
        return self.name

