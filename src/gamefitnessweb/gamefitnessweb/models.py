from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class users(AbstractUser):

    class Meta:
        db_table = "users"
    height = models.DecimalField(max_digits=5,decimal_places=2)
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=200)
    REQUIRED_FIELDS = ['height', 'email', 'weight']
class games(models.Model):
    class Meta:
        db_table = "games"
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=50)
    game_description = models.CharField(max_length=1000, default='')

class exercises(models.Model):
    class Meta:
        db_table = "exercises"
    game_id = models.ForeignKey(games, on_delete=models.CASCADE)
    INJURY_LIST = (('shoulder, back, knee', "tennis"), ('elbow, wrist, shoulder, lumbar', 'golf'), ('ankle, knee', 'soccer'), ('ankle, knee', 'basketball'), ('knee, shoulder', 'baseball'), ('knee, ankle', 'badminton'), ('ankle, shoulder, back', 'volleyball'))
    bodypart = models.CharField(choices=INJURY_LIST, max_length=50)
    exercise_list = models.CharField(max_length=300)
    reps = models.CharField(max_length=300)
    video_link = models.CharField(max_length=500)
    body_part = models.CharField(max_length=50)

class feedback(models.Model):
    class Meta:
        db_table = "feedback"
    RPE_CHOICES = (('0', '0 = no activity'), ('1', '1 = very easy'), ('2', '2 = easy'), ('3', '3 = moderate'), ('4', '4 = somewhat hard'), ('5', '5 = hard'), ('6', '6 = very hard'), ('7', '7 = maximal'))
    rate_of_percieved_exertion = models.CharField(choices=RPE_CHOICES,max_length=50)
