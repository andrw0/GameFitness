# Generated by Django 2.2.6 on 2019-11-07 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(choices=[('Tennis', 'tennis'), ('Golf', 'golf'), ('Soccer', 'soccer'), ('Basketball', 'basketball'), ('Baseball', 'baseball'), ('Football', 'football'), ('Badminton', 'badminton'), ('Volleyball', 'volleyball')], max_length=50)),
            ],
            options={
                'db_table': 'games',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=50)),
                ('height', models.DecimalField(decimal_places=2, max_digits=2)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('game_id', models.CharField(choices=[('Tennis', 'tennis'), ('Golf', 'golf'), ('Soccer', 'soccer'), ('Basketball', 'basketball'), ('Baseball', 'baseball'), ('Football', 'football'), ('Badminton', 'badminton'), ('Volleyball', 'volleyball')], max_length=50)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodypart', models.CharField(choices=[('shoulder, back, knee', 'tennis'), ('elbow, wrist, shoulder, lumbar', 'golf'), ('ankle, knee', 'soccer'), ('ankle, knee', 'basketball'), ('knee, shoulder', 'baseball'), ('knee, ankle', 'badminton'), ('ankle, shoulder, back', 'volleyball')], max_length=50)),
                ('exercise_list', models.CharField(max_length=300)),
                ('reps', models.CharField(max_length=300)),
                ('video_link', models.CharField(max_length=500)),
                ('body_part', models.CharField(max_length=50)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamefitnessweb.games')),
            ],
            options={
                'db_table': 'exercises',
                'managed': True,
            },
        ),
    ]
