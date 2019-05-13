from django import forms
from events_generator.models import FrequenceConfiguration


class EventsGeneratorForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            f = FrequenceConfiguration.objects.get(pk=1)
            frequence = f.frequence
        except:
            frequence = 1
        self.fields['frequence'].initial = frequence

    class Meta:
        model = FrequenceConfiguration
        fields = ('frequence', )

    frequence = forms.IntegerField(min_value=1, label="Frequência em minutos de geração de eventos")
