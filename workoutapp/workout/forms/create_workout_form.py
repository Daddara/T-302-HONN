from django import forms
from ..models import Workout, Exercise


class CreateWorkoutForm():
    name = forms.CharField(max_length=30, help_text='Required.')
    exercises = forms.model_to_dict(Exercise, fields=None, exclude=None)
    created_at = forms.DateField(required=True)

    class Meta:
        model = Workout
        fields = ('workout_name', 'category', 'user', 'created_at', 'image', 'likes', 'dislikes')

