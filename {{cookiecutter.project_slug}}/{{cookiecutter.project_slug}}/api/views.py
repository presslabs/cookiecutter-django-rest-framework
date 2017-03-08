from django.contrib.auth import get_user_model
from rest_framework import viewsets

from {{ cookiecutter.project_slug }}.api.serializers import UserSerializer

User = get_user_model()


class User(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
