from django import forms
from ..models import WorkoutRating, RatingValue


class RateWorkoutForm(forms.ModelForm):
    workout_id = forms.IntegerField(required=True)
    rating = forms.ChoiceField(choices=RatingValue.choices, required=True)

    class Meta:
        model = WorkoutRating
        exclude = ['Judge', 'SubmittedAt']
        fields = ('workout_id', 'rating')