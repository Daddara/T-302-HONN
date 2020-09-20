from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Workout, WorkoutManager, Exercise
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm


def create_workout(request):
    if request.method == 'POST':
        workout_form = CreateWorkoutForm(data=request.POST, instance=Workout())
        # workout_man_form = WorkoutManagerForm(instance=WorkoutManager())
        if workout_form.is_valid():
            name = workout_form.cleaned_data['Name']
            category = workout_form.cleaned_data['Category']
            image = workout_form.cleaned_data['Image']
            public = workout_form.cleaned_data['Public']
            user = request.user
            workout = Workout(Name=name, Category=category, Image=image, Public=public, User=user)
            workout.save()
            return redirect('../accounts/profile/')

        return render(request, 'Workout/create_workout.html', {
            'form': CreateWorkoutForm(), 'errors': workout_form.errors})

    else:
        workout_form = CreateWorkoutForm(instance=Workout())
    return render(request, 'Workout/create_workout.html',
                  {'workout_form': workout_form})


def edit_workout(request, id=None, template_name='update_workout.html'):
    pass


def create_exercise(request):
    if request.method == 'POST':
        exercise_form = ExerciseForm(data=request.POST)
        if exercise_form.is_valid():
            title = exercise_form.cleaned_data['Title']
            description = exercise_form.cleaned_data['Description']
            image = exercise_form.cleaned_data['Image']
            equipment = exercise_form.cleaned_data['Equipment_id']
            exercise = Exercise(Title=title, Description=description, Creator=request.user,
                                Image=image, Equipment=equipment, Public=True)
            exercise.save()
            return redirect('../accounts/profile/')

        return render(request, 'Exercise/create_exercise.html', {
            'form': ExerciseForm(), 'errors': exercise_form.errors})

    else:
        form = ExerciseForm()
    return render(request, 'Exercise/create_exercise.html', {'form': form})


def edit_exercise(request, id=None, template_name='update_exercise.html'):
    pass