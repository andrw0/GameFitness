from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from gamefitnessweb.views import *
from mixer.backend.django import mixer
import pytest


class TestViews():
    def test_homepage(self):
        path = reverse('homepage')
        request = RequestFactory().get(path)
        response = homepage(request)
        assert response.status_code == 200
