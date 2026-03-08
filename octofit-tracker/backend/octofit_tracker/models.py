from djongo import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
