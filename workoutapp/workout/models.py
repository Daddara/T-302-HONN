from django.db import models


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


class User(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)


class Workout(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(max_length=200)
   user = models.ForeignKey(User, on_delete=models.CASCADE())
   likes = models.IntegerField(max_length=None)
   dislikes = models.IntegerField(max_length=None)
   category = models.ForeignKey(Category, on_delete=models.CASCADE())
   created_at = models.DateTimeField()

   class Meta:
      db_table = "workout"


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE())

    class Meta:
        db_table = "exercise"


class Unit(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)


class WorkoutManager(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE())
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE())
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE())
    reps = models.IntegerField(max_length=10)
    quantity = models.IntegerField(max_length=20)




