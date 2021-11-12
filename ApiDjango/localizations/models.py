from django.db import models

# Create your models here.
class localization(models.Model):
    locale = models.CharField(max_length=50)
    adress = models.CharField(max_length=1000, blank=True, null=True)
    additional_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state + '/' + self.city
