from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rating.models import rating

class rating_serializer(ModelSerializer):
    class Meta:
        model = rating
        fields = ['id','user', 'comments','note','data']


