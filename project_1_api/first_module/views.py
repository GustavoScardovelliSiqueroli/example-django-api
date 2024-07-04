from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from first_module.serializers import UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 5  # Número de itens por página
    page_size_query_param = 'page_size'
    max_page_size = 100  # Tamanho máximo permitido para a página


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = UserPagination  # Configura a classe de paginacao
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']  # Campos pelos quais será permitido filtrar

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(username__icontains=search_query)
        return queryset

