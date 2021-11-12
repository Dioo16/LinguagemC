from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from attrations.models import attrations

class attrations_serializer(ModelSerializer):

    class Meta:
        model = attrations
        fields = ['id','name', 'description','minimumAge','openingHours']



