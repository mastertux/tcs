from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)