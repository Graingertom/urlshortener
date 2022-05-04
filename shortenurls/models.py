from django.db import models

# Create your models here.

class URL(models.Model):
    yourURL = models.CharField(max_length=100)
    shortURL = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.yourURL} {self.shortURL}"
