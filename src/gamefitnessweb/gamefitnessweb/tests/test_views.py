from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from gamefitnessweb.views import homepage
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestViews:
    def test_homepage(self):
        path = reverse('../')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = homepage(request)
        assert response.status_code == 200
