from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import datetime

from dashboard.views import add_like_information_to_workouts
from .forms.rate_workout import RateWorkoutForm
from .models import Workout, WorkoutManager, Exercise, ExerciseRating, RatingValue, WorkoutRating, UnitType
from .forms.create_workout_form import CreateWorkoutForm, WorkoutManagerForm
from .forms.create_exercise_form import ExerciseForm
from .forms.rate_exercise_form import RateExerciseForm


@login_required
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
            return redirect('add exercises', workout_id=workout.id)

        else:
            return render(request, 'workout/create_workout.html', {
                'form': workout_form, 'errors': workout_form.errors})

    else:
        workout_form = CreateWorkoutForm()
    return render(request, 'workout/create_workout.html',
                  {'form': workout_form})


@login_required
def add_exercises(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.user != workout.User:
        return render(request, '404.html', status=404)

    if request.method == 'POST':
        form = WorkoutManagerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add exercises', workout_id=workout_id)
        else:
            return render(request, 'workout/add_exercises.html',
                          context={'form': form, 'errors': form.errors,
                                   'workout_id': workout.id})
    else:
        w_m_instance = WorkoutManager(Workout=workout)
        form = WorkoutManagerForm(instance=w_m_instance)

    return render(request, 'workout/add_exercises.html', {'form': form, 'workout_id': workout.id})


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
            public = exercise_form.cleaned_data['Public']
            exercise = Exercise(Title=title, Description=description, Creator=request.user,
                                Image=image, Equipment=equipment, Public=public)
            exercise.save()
            return redirect('profile', slug=request.user.username)

        return render(request, 'exercise/create_exercise.html', {
            'form': exercise_form, 'errors': exercise_form.errors})

    else:
        form = ExerciseForm()
    return render(request, 'exercise/create_exercise.html', {'form': form})


def update_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.user != exercise.Creator:
        return render(request, '404.html', status=404)

    form = ExerciseForm(request.POST or None, instance=exercise)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('exercise_details', exercise_id=exercise_id)
        else:
            print(form.errors)
    return render(request, 'exercise/update_exercise.html', {'form': form, 'exercise': exercise})


def exercise_details(request, exercise_id):
    try:
        exercise = get_object_or_404(Exercise, pk=exercise_id)
    except Exercise.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'exercise/exercise_details.html', context={'exercise_details': exercise})


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


def workout_details(request, workout_id):
    try:
        workout = get_object_or_404(Workout, pk=workout_id)
    except Workout.DoesNotExist:
        return HttpResponse(status=404)
    try:
        managers = WorkoutManager.objects.filter(Workout=workout)
    except Workout.DoesNotExist:
        return HttpResponse(status=404)

    if not workout.Public:
        if workout.User != request.user:
            return HttpResponse(status=404)

    workout = add_like_information_to_workouts(request, [workout])[0]
    return render(request, 'workout/workout_details.html', context={'workout': workout, 'managers': managers})


@login_required
def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, Creator=request.user, pk=exercise_id)
    exercise.delete()

    return redirect('user_exercises')


@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, User=request.user, pk=workout_id)
    workout.delete()

    return redirect('user_workouts')


@login_required
def remove_exercise(request, workout_id, exercise_id):
    """Removes exercise from a given workout"""
    workout = get_object_or_404(Workout, pk=workout_id, User=request.user)
    wm = get_object_or_404(WorkoutManager, Exercise=exercise_id, Workout=workout_id)
    wm.delete()
    return redirect('workout_details', workout_id=workout_id)


def get_all_exercises_json(request):
    exercises = Exercise.objects.all()
    units = UnitType.objects.all()
    ret_dict = {'exercises': {}, 'units': {}}

    for exercise in exercises:
        ret_dict['exercises'][exercise.id] = exercise.Title

    for unit in units:
        print(unit.Name + " "+str(unit.Unit))
        ret_dict['units'][unit.id] = unit.Name + ": "+str(unit.Unit)

    return JsonResponse(data=ret_dict, status=200)


@login_required
def add_exercise_to_workout(request, workout_id, exercise_id, unit_id, amount):
    workout = get_object_or_404(Workout, pk=workout_id, User=request.user)
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    unit = get_object_or_404(UnitType, pk=unit_id)
    new_wm = WorkoutManager.objects.create(Exercise=exercise, Workout=workout, Unit=unit, Quantity=amount)
    new_wm.save()
    return redirect('workout_details', workout_id=workout_id)

