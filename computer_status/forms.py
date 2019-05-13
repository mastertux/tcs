from django import forms
from computer_status.models import ComputerStatus


class ComputerStatusForm(forms.ModelForm):
    class Meta:
        model = ComputerStatus
        fields = ['nome', 'codigo', ]