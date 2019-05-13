from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from computer.models import Computer
from computer.forms import ComputerForm


class ComputerList(ListView):
    model = Computer


class ComputerCreate(CreateView):
    success_url = reverse_lazy('computer_list')
    form_class = ComputerForm
    template_name = 'computer/computer_form.html'


class ComputerUpdate(UpdateView):
    model = Computer
    form_class = ComputerForm
    success_url = reverse_lazy('computer_list')


class ComputerDelete(DeleteView):
    model = Computer
    success_url = reverse_lazy('computer_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

