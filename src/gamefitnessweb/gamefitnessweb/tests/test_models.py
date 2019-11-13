from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:
    def test_users(self):
        person = mixer.blend(
        'gamefitnessweb.users', password = 'test', first_name = 'Andrew',
        last_name = 'Shults', email_address = 'andrew.shults@cgu.edu',
        height = 6, gender = 'M', weight = 170
        )
        assert person.users == True
