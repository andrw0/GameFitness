from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

class users(models.Model):
    password = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    height = models.DecimalField(max_digits=2,decimal_places=2)
    weight = models.DecimalField(max_digits=3,decimal_places=2)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES,max_length=20)
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=50)

