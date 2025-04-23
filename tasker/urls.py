from django.urls import path, include

from tasker.logging import LogOutView
from tasker.views import *


urlpatterns = [
    path("", index, name="index"),
    path("workers/create/",
         WorkerCreateView.as_view(),
         name="worker-create"
         ),
    path("workers/<int:pk>/",
         WorkerDetailView.as_view(),
         name="worker-detail"
         ),
    path("workers/<int:pk>/delete/",
         WorkerDeleteView.as_view(),
         name="worker-delete"
         ),
    path("workers/<int:pk>/update/",
         WorkerPositionUpdateView.as_view(),
         name="worker-update"
         ),
    path("workers/",
         WorkerListView.as_view(),
         name="worker-list"
         ),
    path("positions/",
         PositionListView.as_view(),
         name="position-list"
         ),
    path("positions/create/",
         PositionCreateView.as_view(),
         name="position-create"
         ),
    path("positions/<int:pk>/delete/",
         PositionDeleteView.as_view(),
         name="position-delete"
         ),
    path("positions/<int:pk>/update/",
         PositionUpdateView.as_view(),
         name="position-update"
         ),
    path("projects/",
         ProjectListView.as_view(),
         name="project-list"
         ),
    path("projects/create/",
         ProjectCreateView.as_view(),
         name="project-create"
         ),
    path("projects/<int:pk>/delete/",
         ProjectDeleteView.as_view(),
         name="project-delete"
         ),
    path("projects/<int:pk>/update/",
         ProjectUpdateView.as_view(),
         name="project-update"
         ),
    path("projects/<int:pk>/toggle_done/",
         ProjectToggleDoneView.as_view(),
         name="project-toggle-done"
         ),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"
         ),
    path("tasks/",
         TaskListView.as_view(),
         name="task-list"
         ),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"
         ),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path("tasks/<int:pk>/toggle_done/",
         TaskToggleDoneView.as_view(),
         name="task-toggle-done"
         ),
    path("tasktypes/create/",
         TaskTypeCreateView.as_view(),
         name="tasktype-create"
         ),
    path("tasktypes/",
         TaskTypeListView.as_view(),
         name="tasktype-list"
         ),
    path("tasktypes/<int:pk>/update/",
         TaskTypeUpdateView.as_view(),
         name="tasktype-update"
         ),
    path("tasktypes/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(),
         name="tasktype-delete"
         ),
    path("teams/create/",
         TeamCreateView.as_view(),
         name="team-create"
         ),
    path("teams/",
         TeamListView.as_view(),
         name="team-list"
         ),
    path("teams/<int:pk>/delete/",
         TeamDeleteView.as_view(),
         name="team-delete"
         ),
    path("teams/<int:pk>/update/",
         TeamUpdateView.as_view(),
         name="team-update"
         ),
    path("teams/<int:pk>/toggle_done/",
         TeamToggleDoneView.as_view(),
         name="team-toggle-done"
         ),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', LogOutView.as_view(), name='logout_user'),

]

app_name = "tasker"
