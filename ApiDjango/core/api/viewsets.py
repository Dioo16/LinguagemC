from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import ponto_turisticos
from .serializers import ponto_turisticos_serializer
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSet(ModelViewSet):
    #permission_classes = [DjangoModelPermissions,] #IsAuthenticated é a mais usada, mas, djangoPermission tbm é boa
    serializer_class = ponto_turisticos_serializer
    authentication_classes = [TokenAuthentication]

    filter_backends = [SearchFilter,]
    search_fields  = ['Name', '^Description']
    lookup_field = 'Name' #Serve para alterar o tipo de dado que vai ser  usado para filtrar cada dado json da API
    #Precisa ser unique se não dá conflito

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        Name  = self.request.query_params.get('Name', None)
        Description = self.request.query_params.get('Description', None)
        queryset = ponto_turisticos.objects.all()

        if id:
            queryset = ponto_turisticos.objects.filter(pk=id)

        if Name:
            queryset.filter(Name=Name)

        if Description:
            queryset.filter(Description=Description)

        return queryset



    #def list(self, request, *args, **kwargs):
        #queryset = ponto_turisticos.objects.all()
        #serializers = ponto_turisticos_serializer(queryset, many=True)
        #return Response(serializers)


#SOBRE ESCREVENDO AS FUNÇÕES MÃE.
    #def create(self, request, *args, **kwargs):
        #return Response({'Hello': request.data['Name']})

    #def destroy(self, request, *args, **kwargs):
        #return  Response({'Deleting': request.data['id']})

    #def retrieve(self, request, *args, **kwargs):

    #def update(self, request, *args, **kwargs):

   # def partial_update(self, request, *args, **kwargs):

    #@action(methods=['get'], detail=True)
    #def report(self, request, pk=None):
        #return Response({'Reporting':123})

