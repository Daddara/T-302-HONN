from django import forms
from ..models import Exercise, Equipment


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('Title', 'Description', 'Image', 'Equipment', 'muscle_group')