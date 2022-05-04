from django.db import models

# Create your models here.

class URL(models.Model):
    yourURL = models.CharField(max_length=100)

    def __str__(self):
        return self.name
