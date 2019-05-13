from django.db import models


class ComputerStatus(models.Model):
    codigo = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=60, null=False, blank=False)
