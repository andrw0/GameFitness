from django import forms
from django.forms import ModelForm
from .models import users, games, exercises, feedback
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Create the form class
class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = users
        fields = ['username','first_name','last_name','email','height','weight','gender']
        exclude = ['game_id']

class UserChangeForm(UserChangeForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = users
        fields = ['username','email']
        exclude = ['game_id']


class GameForm(forms.ModelForm):
    class Meta:
        model = games
        fields = ['game_id']
        exclude = ['game_id']

class ExercisesForm(forms.ModelForm):
    class Meta:
        model = exercises
        fields = ['game_id','bodypart','exercise_list','reps','video_link','body_part']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['rate_of_percieved_exertion']
