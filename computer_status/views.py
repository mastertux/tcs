from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import  reverse_lazy
from computer_status.models import ComputerStatus
from computer_status.forms import ComputerStatusForm


class ComputerStatusList(ListView):
    model = ComputerStatus


class ComputerStatusCreate(CreateView):
    success_url = reverse_lazy('computer_status_list')
    form_class = ComputerStatusForm
    template_name = 'computer_status/computerstatus_form.html'


class ComputerStatusUpdate(UpdateView):
    model = ComputerStatus
    form_class = ComputerStatusForm
    success_url = reverse_lazy('computer_status_list')


class ComputerStatusDelete(DeleteView):
    model = ComputerStatus
    success_url = reverse_lazy('computer_status_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
