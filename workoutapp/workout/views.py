from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import Workout, WorkoutManager, Exercise
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm


def create_workout(request):
    if request.method == 'POST':
        workout_form = CreateWorkoutForm(data=request.POST, instance=Workout())
        workout_man_form = [WorkoutManagerForm(data=request.POST, prefix=str(x),
                                               instance=WorkoutManager()) for x in range(0, 3)]
        if workout_form.is_valid() and all[(wm.is_valid() for wm in workout_man_form)]:
            new_workout = workout_form.save()
            for wm in workout_man_form:
                new_wm = wm.save(commit=False)
                new_wm.workout = new_workout
                new_wm.save()
            return redirect('user/placeholder_page.html')

        return render(request, 'createWorkout/create_workout.html', {
            'workout_form': CreateWorkoutForm(), 'workout_man_form': WorkoutManagerForm(), 'errors': workout_form.errors})

    else:
        workout_form = CreateWorkoutForm(instance=Workout)
        workout_man_form = [WorkoutManagerForm(prefix=str(x),
                                               instance=WorkoutManager()) for x in range(0, 3)]
    return render(request, 'createWorkout/create_workout.html',
                  {'workout_form': workout_form , 'workout_man_form': workout_man_form})


def edit_workout(request):


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
