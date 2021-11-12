from rest_framework.viewsets import ModelViewSet
from localizations.models import localization
from .serializers import localization_serializer

class LocalizationsViewSet(ModelViewSet):
    queryset = localization.objects.all()
    serializer_class = localization_serializer