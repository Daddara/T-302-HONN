from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Workout, WorkoutManager, Exercise
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm


def create_workout(request):
    if request.method == 'POST':
        workout_form = CreateWorkoutForm(data=request.POST)
        if workout_form.is_valid():
            name = workout_form.cleaned_data['Name']
            category = workout_form.cleaned_data['Category']
            image = workout_form.cleaned_data['Image']
            public = workout_form.cleaned_data['Public']
            user = request.user
            workout = Workout(Name=name, Category=category, Image=image, Public=public, User=user)
            workout.save()
            return redirect('./add_exercises', workout_id=workout.id)

        else:
            return render(request, 'workout/create_workout.html', {
                'form': CreateWorkoutForm(), 'errors': workout_form.errors})

    else:
        workout_form = CreateWorkoutForm()
    return render(request, 'workout/create_workout.html',
                  {'form': workout_form})


def add_exercises(request, workout_id=None):
    if request.method == 'POST':
        form = WorkoutManagerForm(data=request.POST, instance=WorkoutManager())
        if form.is_valid():
            exercise = form.cleaned_data['Exercise']
            unit = form.cleaned_data['Unit']
            reps = form.cleaned_data['Reps']
            quantity = form.cleaned_data['Quantity']
            workout = Workout.objects.last()
            workout_man = WorkoutManager(Exercise=exercise, Reps=reps, Unit=unit,
                                         Quantity=quantity, Workout=workout)
            workout_man.save()
            return redirect('./add_exercises', workout_id=workout.id)
        else:
            return render(request, 'workout/add_exercises.html', {
                'form': WorkoutManagerForm(), 'errors': form.errors})
    else:
        form = WorkoutManagerForm(instance=WorkoutManager(Workout=workout_id))
    return render(request, 'workout/add_exercises.html',
                  {'form': form})


def edit_workout(request, id=None, template_name='update_workout.html'):
    pass


def create_exercise(request):
    if request.method == 'POST':
        exercise_form = ExerciseForm(data=request.POST)
        if exercise_form.is_valid():
            title = exercise_form.cleaned_data['Title']
            description = exercise_form.cleaned_data['Description']
            image = exercise_form.cleaned_data['Image']
            equipment = exercise_form.cleaned_data['Equipment']
            exercise = Exercise(Title=title, Description=description, Creator=request.user,
                                Image=image, Equipment=equipment, Public=True)
            exercise.save()
            return redirect('profile')

        return render(request, 'exercise/create_exercise.html', {
            'form': exercise_form, 'errors': exercise_form.errors})

    else:
        form = ExerciseForm()
    return render(request, 'exercise/create_exercise.html', {'form': form})


def edit_exercise(request, id=None, template_name='update_exercise.html'):
    pass


def view_created_exercises(request):
    context = {'exercises': Exercise.objects.filter(Creator=request.user)}
    return render(request, 'workout/user_exercises.html', context)
