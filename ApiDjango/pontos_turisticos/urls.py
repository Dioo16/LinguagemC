
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from attrations.api.viewsets import AtrattionsViewSet
from comments_rating.api.viewsets import CommentsViewSet
from rating.api.viewsets import RatingViewSet
from localizations.api.viewsets import LocalizationsViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='ponto_turisticos')
router.register(r'atrattions', AtrattionsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'localizations', LocalizationsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
