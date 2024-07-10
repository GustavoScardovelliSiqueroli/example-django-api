from django.urls import include, path
from rest_framework import routers

from first_module.views import CollaboratorViewSet
from django.urls import path
from knox import views as knox_views
from .knox_p1.login_view import LoginView


router = routers.DefaultRouter()
router.register(r'collaborators', CollaboratorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='knox_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]