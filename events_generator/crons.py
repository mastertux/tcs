from django_cron import CronJobBase, Schedule
from events_generator.models import FrequenceConfiguration
import requests
import json
import random

class GenerateRandomEvents(CronJobBase):
    RUN_EVERY_MINS = FrequenceConfiguration.objects.get(pk=1).frequence
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'events_generator.schedule_events'

    def do(self):
        rc = requests.get('http://localhost:8000/api/computers/')
        computers = json.loads(rc.text)

        rs = requests.get('http://localhost:8000/api/computers_status/')
        status = json.loads(rs.text)

        if rc.status_code == 200 and rc.status_code == 200:
            for computer in computers:
                random_index = random.randrange(0, len(status))
                event = {"codigo": status[random_index].get('codigo'), "computador": computer.get('id')}

                requests.post('http://localhost:8000/api/computer_events/', json=event)
