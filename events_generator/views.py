from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from events_generator.forms import EventsGeneratorForms
from events_generator.models import FrequenceConfiguration


class RandomEventsFrequenceCreate(CreateView):
    success_url = reverse_lazy('dashboard_index')
    form_class = EventsGeneratorForms
    template_name = 'events_generator/events_generator_form.html'


class RandomEventsFrequenceUpdate(UpdateView):
    model = EventsGeneratorForms
    form_class = EventsGeneratorForms
    success_url = reverse_lazy('dashboard_index')