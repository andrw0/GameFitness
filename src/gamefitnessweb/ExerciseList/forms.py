from django import forms

class Exercises(forms.Form):
        exercise = forms.BooleanField(required=False)
