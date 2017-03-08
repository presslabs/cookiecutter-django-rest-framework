import pytest

from django.contrib.auth import get_user_model
from django_dynamic_fixture import G
from rest_framework.test import APIClient


@pytest.fixture
@pytest.mark.django_db
def api_client():
    client = APIClient(format='json')
    user = G(get_user_model())
    client.force_authenticate(user=user)
    return client
