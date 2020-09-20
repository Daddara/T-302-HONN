from django import forms
from ..models import Exercise, Equipment


class ExerciseForm(forms.ModelForm):
    Title = forms.CharField(max_length=30, required=True)
    Description = forms.CharField(max_length=30)
    Image = forms.CharField(max_length=999, required=False)
    Equipment = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=False)
    Public = forms.BooleanField()

    class Meta:
        model = Exercise
        exclude = ['Creator', ]
        fields = ('Title', 'Description', 'Image', 'Equipment', )