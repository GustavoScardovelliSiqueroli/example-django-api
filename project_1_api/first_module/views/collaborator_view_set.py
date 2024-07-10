from rest_framework import viewsets
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from first_module.serializers import  CollaboratorSerializer
from first_module.models import Collaborator
from .paginations.collaborator_pagination import CollaboratorPagination


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all().order_by('name')
    serializer_class = CollaboratorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = CollaboratorPagination  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']  # Campos pelos quais será permitido filtrar

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset