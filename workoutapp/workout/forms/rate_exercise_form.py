from django import forms
from ..models import Exercise, ExerciseRating, RatingValue


class RateExerciseForm(forms.ModelForm):
    exercise_id = forms.IntegerField(required=True)
    rating = forms.ChoiceField(choices=RatingValue.choices, required=True)

    class Meta:
        model = ExerciseRating
        exclude = ['Judge', 'SubmittedAt']
        fields = ('exercise_id', 'rating')