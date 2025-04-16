from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import DateInput

from tasker.models import Position, Worker, TaskType, Task, Team, Project


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search position by name"}
        )
    )


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class WorkerUpdateForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["position"]


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
        attrs={"placeholder": "Search worker by username"}
        )
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search task type by name"}
        )
    )


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',}),
        help_text='Select a date',
        input_formats=["%Y-%m-%d"],

    )
    class Meta:
        model = Task
        fields = "__all__"



class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search task by name"}
        )
    )


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search team by name"}
        )
    )


class ProjectForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',}),
        help_text='Select a date',
        input_formats=["%Y-%m-%d"],
    )
    class Meta:
        model = Project
        fields = "__all__"


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search project by name"}
        )
    )
