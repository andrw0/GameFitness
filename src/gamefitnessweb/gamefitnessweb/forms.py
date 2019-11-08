from django import forms
from django.forms import ModelForm
from .models import users, games, exercises

# Create the form class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = users
        fields = ['first_name','last_name','email_address','password','height','weight','gender']
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
