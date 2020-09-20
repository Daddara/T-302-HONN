from django import forms
from ..models import Workout, Exercise, WorkoutManager, UnitType, Category, User


class CreateWorkoutForm(forms.ModelForm):
    workout_name = forms.CharField(max_length=30, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.ImageField()

    class Meta:
        model = Workout
        fields = ('workout_name', 'category', 'image')


class WorkoutManagerForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    unit = forms.ModelChoiceField(queryset=UnitType.objects.all())
    reps = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = WorkoutManager
        exclude = ('workout', )
        fields = ('exercise', 'unit', 'reps', 'quantity')