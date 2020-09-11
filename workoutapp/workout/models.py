from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=20, default="", unique=True)

class Workout(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=20, default="")
    CreatedAt = models.DateTimeField(auto_now=True)
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)
    Public = models.BooleanField(default=False)

class Comment(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=250, default="")

class Equipment(models.Model):
    Name = models.CharField(max_length=20, default="")
    Description = models.CharField(max_length=250, default="")
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")

class Exercise(models.Model):
    Title = models.CharField(max_length=20, default="")
    Creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Description = models.CharField(max_length=250, default="")
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    Equipment = models.ForeignKey(Equipment, null=True, on_delete=models.SET_NULL)
    Public = models.BooleanField(default=False)
    class Meta:
        unique_together = ('Creator', 'Title',)

class UnitType(models.Model):
    Name = models.CharField(max_length=20, default="")
    Unit = models.CharField(max_length=20, default="")

class WorkoutManager(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Exercise, null=True, on_delete=models.SET_NULL)
    Unit = models.ForeignKey(UnitType, null=True, on_delete=models.SET_NULL)
    Reps = models.IntegerField(default=0)
    Quantity = models.IntegerField(default=0)


