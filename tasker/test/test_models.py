from django.contrib.auth import get_user_model
from django.test import TestCase

from tasker.models import Position, TaskType, Task, Team, Project


class ModelTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="test position",
            )
        f_str = f"{position.name}"
        self.assertEqual(str(position), f_str)

    # def test_driver_str_and_license(self):
    #     driver = get_user_model().objects.create(
    #         username="testusername",
    #         password="pass",
    #         first_name="test_first_name",
    #         last_name="test_last_name",
    #         license_number="test_license_number",
    #     )
    #     f_str = f"{driver.username} ({driver.first_name} {driver.last_name})"
    #     self.assertEqual(
    #         str(driver),
    #         f_str)
    #     self.assertEqual(driver.license_number, "test_license_number")
    #
    def test_tasktype_task_str(self):
        tasktype = TaskType.objects.create(name="test task type")
        task = Task.objects.create(name="test task", description="test_description")
        task.save()
        task.task_types.add(tasktype)
        task.save()
        self.assertEqual(str(task), task.name)
        # self.assertEqual(str(tasktype), task.task_types.name)


    def test_tasktype_str(self):
        tasktype = TaskType.objects.create(name="test task type")
        self.assertEqual(str(tasktype), tasktype.name)

    def test_team_str(self):
        team = Team.objects.create(name="test team")
        self.assertEqual(str(team), team.name)

    def test_project_str(self):
        project = Project.objects.create(name="test project")
        self.assertEqual(str(project), project.name)



