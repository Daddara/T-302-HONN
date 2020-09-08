from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=250, blank=False)

class Workout(models.Model):
    User = models.ForeignKey(User,  on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Name = models.CharField(max_length=250, blank=True)
    CreatedAt = models.DateField(blank=True)
    Image = models.CharField(max_length=250, blank=True)
    Likes = models.IntegerField(blank=True)
    Dislikes = models.IntegerField(blank=True)

class Comment(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=250, blank=True)

class Equipment(models.Model):
    Name = models.CharField(max_length=250, blank=True)
    Description = models.CharField(max_length=250, blank=True)
    Image = models.CharField(max_length=250, blank=True)

class Exercise(models.Model):
    Title = models.CharField(max_length=250, blank=True)
    Description = models.CharField(max_length=250, blank=True)
    Image = models.CharField(max_length=250, blank=True)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class UnitType(models.Model):
    Name = models.CharField(max_length=250, blank=True)
    Unit = models.CharField(max_length=250, blank=True)

class WorkoutManager(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    Unit = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    Reps = models.IntegerField(blank=True)
    Quantity = models.IntegerField(blank=True)