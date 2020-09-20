from django import forms
from ..models import Exercise, Equipment

class ExerciseForm(forms.Form):
    Title = forms.CharField(max_length=30, required=True)
    Description = forms.CharField(max_length=30)
    Image = forms.CharField(max_length=999, required=False)
    Equipment_id = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=False)
    class Meta:
        model = Exercise
        exclude = ['user', ]
        fields = ('title', 'description', 'image', 'equipment')