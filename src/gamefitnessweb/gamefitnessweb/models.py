from django.db import models

# Create your models here.

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

    class Meta:
        db_table = 'users'
        managed = True

class games(models.Model):
    GAME_CHOICES = (('Tennis','tennis'),('Golf','golf'),('Soccer','soccer'),('Basketball','basketball'),('Baseball','baseball'),('Football','football'),('Badminton','badminton'),('Volleyball','volleyball'))
    game_id = models.CharField(choices=GAME_CHOICES,max_length=50)

    class Meta:
        db_table = 'games'
        managed = True

class exercises(models.Model):
    game_id = models.ForeignKey(games, on_delete=models.CASCADE)
    INJURY_LIST = (('shoulder, back, knee', "tennis"), ('elbow, wrist, shoulder, lumbar', 'golf'), ('ankle, knee', 'soccer'), ('ankle, knee', 'basketball'), ('knee, shoulder', 'baseball'), ('knee, ankle', 'badminton'), ('ankle, shoulder, back', 'volleyball'))
    bodypart = models.CharField(choices=INJURY_LIST, max_length=50)
    exercise_list = models.CharField(max_length=300)
    reps = models.CharField(max_length=300)
    video_link = models.CharField(max_length=500)
    body_part = models.CharField(max_length=50)

    class Meta:
        db_table = 'exercises'
        managed = True
