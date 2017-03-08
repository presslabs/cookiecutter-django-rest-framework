# Define here functions wihch take a model an return it's serialized form
from rest_framework.reverse import reverse


def absolute_reverse(*args, **kwargs):
    return 'http://testserver{}'.format(reverse(*args, **kwargs))


def user(user):
    return {
        "id": user.id,
        "url": absolute_reverse('user-detail', kwargs={'pk': user.id}),
        "username": user.username
    }
