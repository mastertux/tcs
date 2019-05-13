from django import forms
from computer.models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['name', ]