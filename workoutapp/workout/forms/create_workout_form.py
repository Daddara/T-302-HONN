from django import forms
from ..models import Workout, Exercise, WorkoutManager, UnitType, Category, User


class CreateWorkoutForm(forms.ModelForm):
    Name = forms.CharField(max_length=30, required=True)
    Category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    Image = forms.CharField(max_length=999, required=False)
    Public = forms.BooleanField(required=False)

    class Meta:
        model = Workout
        exclude = ['User', 'CreatedAt', 'Likes', 'Dislikes', ]
        fields = ('Name', 'Category', 'Image', 'Public', )


class WorkoutManagerForm(forms.ModelForm):
    Unit = forms.ModelChoiceField(queryset=UnitType.objects.all())
    Reps = forms.IntegerField(required=True)
    Quantity = forms.IntegerField(required=True)

    class Meta:
        model = WorkoutManager
        exclude = ['Workout', 'Exercise', ]
        fields = ('Exercise', 'Unit', 'Reps', 'Quantity', )