from django.db import models


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"
