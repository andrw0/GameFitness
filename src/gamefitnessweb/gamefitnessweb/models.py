from django.db import models

# Create your models here.

class users(models.Model):

    class Meta:
        db_table = "users"
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    height = models.DecimalField(max_digits=5,decimal_places=2)
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=200)

class games(models.Model):
    class Meta:
        db_table = "games"
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=50)

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
