from django import forms
from ..models import Exercise, Equipment

class ExerciseForm(forms.Form):
    title = forms.CharField(max_length=30, required=True)
    description = forms.CharField(max_length=30)
    image = forms.ImageField()
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all())
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'image', 'equipment')