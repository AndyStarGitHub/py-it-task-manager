from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasker.models import Position, TaskType, Worker, Task


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


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("is_completed", "-created_at",)

    fieldsets = (
        (("Additional info", {"fields": ("created_at", "is_completed",)}),)
    )
    add_fieldsets = (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "created_at",
                        "is_completed",
                    )
                },
            ),
        )
    )

