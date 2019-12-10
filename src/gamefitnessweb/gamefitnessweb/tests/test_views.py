from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from gamefitnessweb.views import *
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestViews():
    def test_homepage(self):
        path = reverse('homepage')
        request = RequestFactory().get(path)
        response = homepage(request)
        assert response.status_code == 200

    def test_feedback(self):
        path = reverse('feedback')
        request = RequestFactory().get(path)
        response = showFeedbackForm(request)
        assert response.status_code == 200

    def test_games(self):
        path = reverse('games')
        request = RequestFactory().get(path)
        response = showGameForm(request)
        assert response.status_code == 200

    def test_exercises(self):
        path = reverse('exercisesList')
        request = RequestFactory().get(path)
        response = showExercisesForm(request)
        assert response.status_code == 200
