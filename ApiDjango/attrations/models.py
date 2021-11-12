from django.db import models

class attrations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    openingHours = models.TimeField(auto_now=False)
    minimumAge = models.IntegerField()

    def __str__(self):
        return self.name



