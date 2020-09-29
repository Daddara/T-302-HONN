from django.contrib import admin

# Register your models here.
from workout.models import Exercise, Workout, WorkoutManager, Category, Equipment, MuscleGroup

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutManager)
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(MuscleGroup)