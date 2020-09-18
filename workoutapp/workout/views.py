from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .forms.create_workout_form import WorkoutForm, WorkoutManagerForm, ExerciseForm


def index(request):
    return HttpResponse ("Example")


def create_workout(request):
    if request.method == 'POST':
        workout_form = WorkoutForm(data=request.POST)
        workout_man_form = WorkoutManagerForm(data=request.POST)
        exercise_form = ExerciseForm(data=request.POST)
        if workout_form.is_valid() and workout_man_form.is_valid() and exercise_form.is_valid():
            workout_form.save()
            workout_man_form.save()
            exercise_form.save()
            workout_man_form.workout = workout_form
            return redirect('user/placeholder_page.html')

        return render(request, 'createWorkout/create_workout.html', {
            'form': WorkoutForm(), 'errors': workout_form.errors})

    else:
        form = WorkoutForm()
    return render(request, 'createWorkout/create_workout.html', {'form': form})
