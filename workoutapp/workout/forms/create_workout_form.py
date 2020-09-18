from django import forms
from ..models import Workout, Exercise, WorkoutManager


class WorkoutForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    created_at = forms.DateField(required=True)

    class Meta:
        model = Workout
        fields = ('workout_name', 'category', 'user', 'created_at', 'image', 'likes', 'dislikes')


class WorkoutManagerForm(forms.Form):
    class Meta:
        model = WorkoutManager
        fields = ('workout', 'exercise', 'unit', 'reps', 'quantity')


class ExerciseForm(forms.Form):
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'image', 'equipment')
