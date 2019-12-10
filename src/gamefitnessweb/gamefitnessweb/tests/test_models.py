from mixer.backend.django import mixer
import pytest
from gamefitnessweb.models import users, games

@pytest.mark.django_db
class TestUserModels:
    def test_users(self):
        person = mixer.blend(
        'gamefitnessweb.users', first_name = 'Andrew',
        last_name = 'Shults', email_address = 'andrew.shults@cgu.edu',
        height = 6, gender = 'M', weight = 150,
        )
        assert person.first_name == "Andrew", person.last_name == "Shults"


@pytest.mark.django_db
class TestGamesModel:
    def test_games(self):
        list_games = mixer.blend(
        'gamefitnessweb.games', game_id = """'Tennis', 'Golf', 'Baseball',
        'Badminton', 'Soccer', 'Basketball',
        'Volleyball', 'Football'"""
        )
        assert list_games.game_id == """'Tennis', 'Golf', 'Baseball',
        'Badminton', 'Soccer', 'Basketball',
        'Volleyball', 'Football'"""
