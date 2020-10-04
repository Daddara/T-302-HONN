from django import forms
from ..models import Workout, Exercise, WorkoutManager, UnitType, Category, User


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('Name', 'Category', 'Image', 'Public', 'short_description', 'workout_goal')


class WorkoutManagerForm(forms.ModelForm):
    class Meta:
        model = WorkoutManager
        exclude = []
        widgets = {
            'Workout': forms.HiddenInput(attrs={'readonly': 'True'})
        }