from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasker.models import TaskType, Worker, Task, Team, Project, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ("is_completed", "deadline",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("is_completed", "deadline",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ordering = ("-is_active", "name",)
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
