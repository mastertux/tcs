from django.shortcuts import render
from computer_events.models import ComputerEvents

def index(request):
    events = ComputerEvents.objects.distinct('computer_id').order_by('-computer_id','-created_at')

    return render(request, 'dashboard/index.html', context={'events': events})
