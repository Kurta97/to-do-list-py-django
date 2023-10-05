from django import forms
from .models import Task


class TaskBasedForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'datetime-local'})
    )


class TaskCreateForm(TaskBasedForm):
    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateForm(TaskBasedForm):
    class Meta:
        model = Task
        fields = ("deadline", )