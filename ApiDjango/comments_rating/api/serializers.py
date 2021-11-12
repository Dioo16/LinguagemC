from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from comments_rating.models import comments

class comments_serializer(ModelSerializer):
    class Meta:
        model = comments
        fields = ['id','users', 'comments','data','approved']


