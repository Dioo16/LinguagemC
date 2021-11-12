from rest_framework.viewsets import ModelViewSet
from comments_rating.models import comments
from .serializers import comments_serializer

class CommentsViewSet(ModelViewSet):
    queryset = comments.objects.all()
    serializer_class = comments_serializer