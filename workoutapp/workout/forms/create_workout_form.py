from django import forms
from ..models import Workout, Exercise, WorkoutManager, UnitType, Category, User


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('Name', 'Category', 'Image', 'Public', 'short_description', 'workout_goal')


class WorkoutManagerForm(forms.ModelForm):
    Exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), required=False)
    Unit = forms.ModelChoiceField(queryset=UnitType.objects.all(), required=False)
    Reps = forms.IntegerField(required=True)
    Quantity = forms.IntegerField(required=True)

    class Meta:
        model = WorkoutManager
        exclude = ['Workout', ]
        fields = ('Exercise', 'Unit', 'Reps', 'Quantity', )