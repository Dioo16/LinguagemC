from django_filters import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from attrations.models import attrations
from .serializers import attrations_serializer

class AtrattionsViewSet(ModelViewSet):
    queryset = attrations.objects.all()
    serializer_class = attrations_serializer
    filter_backends = [SearchFilter,]
    search_fields  = ['^name']