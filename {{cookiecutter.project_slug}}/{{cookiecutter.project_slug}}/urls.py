from rest_framework import routers

from {{ cookiecutter.project_slug }}.api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', views.User, 'user')

urlpatterns = router.urls
