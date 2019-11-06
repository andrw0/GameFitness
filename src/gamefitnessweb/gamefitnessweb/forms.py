from django import forms
from django.forms import ModelForm
from gamefitnessweb.models import users, games

# Create the form class
class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ['password','first_name','last_name','email_address','height','weight','gender']

# Create a form to add a user info
form = UserForm()

# Create a form to change an existing user information
userInfo = users.objects.get(pk=1)
form = UserForm(instance=userInfo)

class GameForm(ModelForm):
    class Meta:
        model = games
        fields = ['game_id']

form = GameForm()

gameInfo = users.objects.get(pk=1)
form = GameForm(instance=gameInfo)
