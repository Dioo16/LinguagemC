from django.db import models
from django.contrib.auth.models import User

class comments(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    data = models.DateField(auto_now=True)
    approved = models.BooleanField()

    def __str__(self):
        return self.users.first_name


