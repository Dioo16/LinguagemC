from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from localizations.models import localization

class localization_serializer(ModelSerializer):
    class Meta:
        model = localization
        fields = ['id','locale', 'adress','additional_address','city','state']


