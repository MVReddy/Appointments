from django.db import models

# Create your models here.


class Schedule(models.Model):
    appointment_date = models.DateField(name='DATE')
    appointment_time = models.TimeField(name="TIME")
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description

