from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
import datetime

from .forms.rate_workout import RateWorkoutForm
from .models import Workout, WorkoutManager, Exercise, ExerciseRating, RatingValue, WorkoutRating
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm
from .forms.rate_exercise_form import RateExerciseForm


def create_workout(request):
    if request.method == 'POST':
        workout_form = CreateWorkoutForm(data=request.POST)
        if workout_form.is_valid():
            name = workout_form.cleaned_data['Name']
            category = workout_form.cleaned_data['Category']
            image = workout_form.cleaned_data['Image']
            public = workout_form.cleaned_data['Public']
            description = workout_form.cleaned_data['short_description']
            goal = workout_form.cleaned_data['workout_goal']
            user = request.user
            workout = Workout(Name=name, Category=category, Image=image, Public=public, User=user,
                              short_description=description, workout_goal=goal)
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


@csrf_exempt
def rate_exercise(request):
    if not request.user.is_authenticated:
        print("request.user.is_authenticated")
        return HttpResponse(status=401)

    if request.method == 'POST':
        form = RateExerciseForm(data=request.POST)
        if not form.is_valid():
            return HttpResponse(status=400)
        
        # Get values
        exercise_id = form.cleaned_data['exercise_id']
        rating_value = form.cleaned_data['rating']
        
        # Test if exercise exists
        exercise = None
        try:
            exercise = Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return HttpResponse(status=404)

        # Get or create rating
        rating = ExerciseRating.objects.get_or_create(
            Exercise=exercise,
            Judge=request.user
        )[0]

        # Save rating
        rating.Rating = rating_value
        rating.SubmittedAt = datetime.datetime.now()
        rating.save()

        # Be Happy 
        return HttpResponse(status=200)


@csrf_exempt
def rate_workout(request):
    if not request.user.is_authenticated:
        print("request.user.is_authenticated")
        return HttpResponse(status=401)

    if request.method == 'POST':
        form = RateWorkoutForm(data=request.POST)
        if not form.is_valid():
            return HttpResponse(status=400)

        # Get values
        workout_id = form.cleaned_data['workout_id']
        rating_value = form.cleaned_data['rating']

        # Test if workout exists
        workout = None
        try:
            workout = Workout.objects.get(id=workout_id)
        except Workout.DoesNotExist:
            return HttpResponse(status=404)

        # Get or create rating
        print()
        rating = WorkoutRating.objects.get_or_create(
            Workout=workout,
            Judge=request.user
        )[0]

        # Save rating
        rating.Rating = rating_value
        rating.SubmittedAt = datetime.datetime.now()
        rating.save()

        # Be Happy
        return HttpResponse(status=200)