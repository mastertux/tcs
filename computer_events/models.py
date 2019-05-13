from django.db import models


class ComputerEvents(models.Model):
    computer = models.ForeignKey('computer.Computer', on_delete=models.CASCADE, blank=False, null=False)
    status = models.ForeignKey('computer_status.ComputerStatus', on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)