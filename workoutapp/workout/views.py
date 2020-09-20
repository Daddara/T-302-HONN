from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm


def create_workout(request):
    if request.method == 'POST':
        workout_form = CreateWorkoutForm(data=request.POST)
        workout_man_form = WorkoutManagerForm(data=request.POST)
        exercise_form = ExerciseForm(data=request.GET)
        if workout_form.is_valid() and workout_man_form.is_valid() and exercise_form.is_valid():
            workout_form.save()
            workout_man_form.save()
            exercise_form.save()
            workout_man_form.workout = workout_form
            workout_man_form.exercise = exercise_form
            return redirect('user/placeholder_page.html')

        return render(request, 'createWorkout/create_workout.html', {
            'form': CreateWorkoutForm(), 'errors': workout_form.errors})

    else:
        form = CreateWorkoutForm()
    return render(request, 'createWorkout/create_workout.html', {'form': form})


def create_exercise(request):
    if request.method == 'POST':
        exercise_form = ExerciseForm(data=request.POST)
        if exercise_form.is_valid():
            exercise_form.save()
            return redirect('user/placeholder_page.html')

        return render(request, 'createExercise/create_exercise.html', {
            'form': ExerciseForm(), 'errors': exercise_form.errors})

    else:
        form = ExerciseForm()
    return render(request, 'createExercise/create_exercise.html', {'form': form})
