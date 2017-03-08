import pytest

from django.contrib.auth import get_user_model
from django_dynamic_fixture import G

from {{ cookiecutter.project_slug }}.tests.fixtures import api_client  # noqa: F401
from {{ cookiecutter.project_slug }}.tests.api import specs


@pytest.mark.django_db
def test_basic_request(api_client):
    user = G(get_user_model())
    response = api_client.get('/users/{}'.format(user.id))

    assert response.status_code == 200
    assert response.data == specs.user(user)
