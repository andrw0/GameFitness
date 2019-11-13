from django.urls import reverse, resolve


class TestUrls:
    def test_url_signin(self):
        path = reverse('signin')
        assert resolve(path).view_name == 'signin'

    def test_url_games(self):
        path = reverse('games')
        assert resolve(path).view_name == 'games'

    def test_exercisesList_games(self):
        path = reverse('exercisesList')
        assert resolve(path).view_name == 'exercisesList'
