from django.db import models
from attrations.models import attrations
from comments_rating.models import comments
from rating.models import  rating
from localizations.models import localization

class ponto_turisticos(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Approved = models.BooleanField(default=False)
    Attrations = models.ManyToManyField(attrations)
    Comments = models.ManyToManyField(comments)
    Rating = models.ManyToManyField(rating)
    Adress = models.ForeignKey(localization, on_delete=models.CASCADE, null=True, blank=True)
    Photo = models.ImageField(upload_to='imagens_pontos_turísticos', null=True, blank=True)
    def __str__(self):
        return self.Name

    @property #Outro método sem mexer no serializer
    def name_aprove2(self):
        return '%s - %s' % (self.Name, self.Approved)



