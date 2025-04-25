from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tasker.models import Position, Project, TaskType, Task, Team

User = get_user_model()


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(name="test_position_21")
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username="admin_21",
            password="tester",
            position=position,
        )
        self.client.force_login(self.admin_user)
        self.worker = User.objects.create_user(
            username="wrk",
            password="worker",
            position=position,
        )

    def test_worker_position_list(self):
        """
        Test that worker's position is in
        list_display on worker admin page.
        :return:
        """

        url = reverse("admin:tasker_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_list(self):
        """
        Test that worker's position is on worker detail admin page.
        :return:
        """

        url = reverse("admin:tasker_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_set_list(self):
        """
        Test that worker's additional info is on worker detail
        admin page in additional fieldsets.
        :return:
        """
        url = reverse("admin:tasker_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, "Additional info")


class ModelTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="test position",
            )
        f_str = f"{position.name}"
        self.assertEqual(str(position), f_str)

    def test_worker_str_and_position(self):
        position = Position.objects.create(
            name="test position",
            )
        worker = User.objects.create(
            username="testusername",
            password="pass",
            first_name="test_first_name",
            last_name="test_last_name",
            position=position,
        )
        f_str = f"{worker.username} ({worker.first_name} {worker.last_name})"
        self.assertEqual(
            str(worker),
            f_str)
        self.assertEqual(worker.position.name, "test position")

    def test_task_str(self):
        task = Task.objects.create(name="test task",
                                   description="test_description"
                                   )
        self.assertEqual(str(task), "test task")

    def test_tasktype_str(self):
        tasktype = TaskType.objects.create(name="test task type")
        self.assertEqual(str(tasktype), "test task type")

    def test_team_str(self):
        team = Team.objects.create(name="test team")
        self.assertEqual(str(team), "test team")

    def test_project_str(self):
        project = Project.objects.create(name="test project")
        self.assertEqual(str(project), "test project")


WORKER_URL = reverse("tasker:worker-list")
POSITION_URL = reverse("tasker:position-list")
TASK_URL = reverse("tasker:task-list")
TASK_TYPE_URL = reverse("tasker:tasktype-list")
PROJECT_URL = reverse("tasker:project-list")
TEAM_URL = reverse("tasker:team-list")


class PublicLoginRequiredTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(WORKER_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(POSITION_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(TASK_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(PROJECT_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(TEAM_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTypesTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(name="test_position")
        self.user = User.objects.create_user(
            username="testuser",
            password="<PASSWsORD>",
            position=position,
        )

    def test_retrieve_tasktypes(self):

        TaskType.objects.create(name="testing manually")
        TaskType.objects.create(name="testing auto")
        self.client.force_login(self.user)
        response = self.client.get(TASK_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(
            list(response.context["tasktype_list"]),
            list(task_types),
        )
        self.assertTemplateUsed(response, "tasker/tasktype_list.html")


class PrivateWorkerTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test_position")
        self.user = User.objects.create_user(
            username="<NAME>",
            password="<PASSWORD>",
            first_name="test",
            last_name="test",
            position=self.position,
        )
        self.client.force_login(self.user)

    def test_create_worker(self):
        form_data = {
            "username": "<NAME>",
            "password1": "<PASSWORD>",
            "password2": "<PASSWORD>",
            "first_name": "test",
            "last_name": "test",
            "position": self.position,
        }
        self.client.post(reverse("tasker:worker-create"), data=form_data)
        new_user = User.objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position, form_data["position"])
