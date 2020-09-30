from django.utils.translation import gettext_lazy as gt
from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=20, default="", unique=True)

    def __str__(self):
        return self.Name


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
    Has_Liked = models.BooleanField(default=False)
    Has_Disliked = models.BooleanField(default=False)

    def __str__(self):
        return self.User.username + ": " + self.Name


class Comment(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.Commenter.username + "'s comment on workout #" + str(self.Workout.id)


class Equipment(models.Model):
    Name = models.CharField(max_length=20, default="")
    Description = models.CharField(max_length=250, default="")
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")

    def __str__(self):
        return self.Name


class MuscleGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    Title = models.CharField(max_length=20, default="")
    Creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Description = models.CharField(max_length=250, default="")
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    Equipment = models.ForeignKey(Equipment, null=True, blank=True, on_delete=models.SET_NULL)
    Public = models.BooleanField(default=False)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, blank=True, on_delete=models.SET_NULL)
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)
    Has_Liked = models.BooleanField(default=False)
    Has_Disliked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('Creator', 'Title',)

    def __str__(self):
        return self.Creator.username + "'s exercise: " + self.Title


class UnitType(models.Model):
    Name = models.CharField(max_length=20, default="")
    Unit = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.Name + ": " + self.Unit


class WorkoutManager(models.Model):
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Exercise, null=True, on_delete=models.SET_NULL)
    Unit = models.ForeignKey(UnitType, null=True, on_delete=models.SET_NULL)
    Reps = models.IntegerField(default=0)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.Workout.Name + ", " + self.Exercise.Title


class RatingValue(models.TextChoices):
    LIKE = '+1', gt('LIKE')
    IDK = '*0', gt('IDK')
    DISLIKE = '-1', gt('DISLIKE')


class ExerciseRating(models.Model):
    Judge = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Exercise, null=False, on_delete=models.CASCADE)
    SubmittedAt = models.DateTimeField(auto_now=True)
    Rating = models.IntegerField(choices=RatingValue.choices, default=0)

    def __str__(self):
        rating = ""
        if self.Rating == 1:
            rating = " likes "
        elif self.Rating == -1:
            rating = " dislikes "
        else:
            rating = "Doesn't know if he likes "

        return self.Judge.username + rating + self.Exercise.Title


class WorkoutRating(models.Model):
    Judge = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    Workout = models.ForeignKey(Workout, blank=True, null=True, on_delete=models.CASCADE)
    SubmittedAt = models.DateTimeField(auto_now=True)
    Rating = models.IntegerField(choices=RatingValue.choices)

    def __str__(self):
        rating = ""
        if self.Rating == "+1":
            rating = "Likes "
        elif self.Rating == "-1":
            rating = "Dislikes "
        else:
            rating = "Doesn't know if he likes "

        return self.Judge.username + rating + self.Workout.Name
