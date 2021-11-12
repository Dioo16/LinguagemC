from rest_framework.viewsets import ModelViewSet
from rating.models import rating
from .serializers import rating_serializer

class RatingViewSet(ModelViewSet):
    queryset = rating.objects.all()
    serializer_class = rating_serializer