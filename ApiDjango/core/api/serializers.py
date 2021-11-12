from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import ponto_turisticos
from attrations.api.serializers import attrations_serializer
from rest_framework.fields import SerializerMethodField

class ponto_turisticos_serializer(ModelSerializer):
    Attrations = attrations_serializer(many=True)
    name_approve = SerializerMethodField()
    class Meta:
        model = ponto_turisticos
        fields = ['id','Name', 'Description', 'Approved', 'Photo', 'Attrations', 'name_approve', 'name_aprove2']


    def get_name_approve(self, obj):
        return '%s - %s' % (obj.Name, obj.Approved)