from django import forms
from ..models import Workout, Exercise, WorkoutManager, UnitType, Category, User



class CreateWorkoutForm(forms.Form):
    workout_name = forms.CharField(max_length=30, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.ImageField()

    class Meta:
        model = Workout
        fields = ('workout_name', 'category', 'user', 'created_at', 'image', 'likes', 'dislikes')


class WorkoutManagerForm(forms.Form):
    workout = forms.ModelChoiceField(queryset=Workout.objects.all())
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    unit = forms.ModelChoiceField(queryset=UnitType.objects.all())
    reps = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = WorkoutManager
        fields = ('workout', 'exercise', 'unit', 'reps', 'quantity')