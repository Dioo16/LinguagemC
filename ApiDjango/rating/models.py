from django.db import models
from django.contrib.auth.models import User

class rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    comments = models.TextField(blank=True, null=True)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username