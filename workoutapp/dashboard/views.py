from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from workout.models import Workout, Exercise, WorkoutRating, ExerciseRating, Category, MuscleGroup, FavouriteExercise, FavouriteWorkout
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
import pytz


def dashboard(request):
    return redirect('public_workouts')

@login_required
def user_exercises(request):
    try:
        user_exercises = Exercise.objects.filter(Creator=request.user)
    except Exercise.DoesNotExist:
        user_exercises = []

    muscle_groups = MuscleGroup.objects.all()
    exercise_updated = add_like_information_to_exercises(request, user_exercises)
    return render(request, 'dashboard/dashboard_exercise.html', context={'exercises': exercise_updated,
                                                                         'muscle_groups': muscle_groups})


@login_required
def user_workouts(request):
    try:
        user_wo = Workout.objects.filter(User=request.user)
    except Exercise.DoesNotExist:
        user_wo = []

    categories = Category.objects.all()
    workouts_updated = add_like_information_to_workouts(request, user_wo)
    return render(request, 'dashboard/dashboard_workout.html', context={'workouts': workouts_updated,
                                                                        'categories': categories})


def workouts(request):
    categories = Category.objects.all()
    context = {'workouts': get_workouts_with_likes(request), 'categories': categories}
    return render(request, 'dashboard/dashboard_workout.html', context)


def exercises(request):
    muscle_groups = MuscleGroup.objects.all()
    context = {'exercises': get_exercises_with_likes(request), 'muscle_groups': muscle_groups}
    return render(request, 'dashboard/dashboard_exercise.html', context)


def filter_ex_public(request, muscle_group):
    muscle_groups = MuscleGroup.objects.all()
    filtered_exercises = filter_exercise_category(muscle_group)
    context = {'exercises': add_like_information_to_exercises(request, filtered_exercises), 'muscle_groups': muscle_groups}
    return render(request, 'dashboard/dashboard_exercise.html', context)


def filter_exercise_category(muscle_group_id: int) -> list:
    try:
        return Exercise.objects.filter(muscle_group=muscle_group_id, Public=True)
    except Exercise.DoesNotExist:
        return []


def filter_wo_public(request, category_id):
    categories = Category.objects.all()
    filtered_workouts = filter_workout_category(category_id)
    context = {'workouts': add_like_information_to_workouts(request, filtered_workouts), 'categories': categories}
    return render(request, 'dashboard/dashboard_workout.html', context)


def filter_workout_category(category: int) -> list:
    try:
        return Workout.objects.filter(Category=category, Public=True)
    except Workout.DoesNotExist:
        return []

@login_required
def favourite_exercise(request):
    fav_exercise = FavouriteExercise.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard_favourites_exercise.html', {'fav_exercise': fav_exercise})


@login_required
def favourites_add_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    try:
        fav_ex = FavouriteExercise.objects.get(exercise=exercise, user=request.user)
        fav_ex.delete()
    except FavouriteExercise.DoesNotExist:
        new_ex = FavouriteExercise.objects.create(exercise=exercise, user=request.user)
        new_ex.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite_workout(request):
    fav_workout = FavouriteWorkout.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard_favourites_workout.html', {'fav_workout': fav_workout})


@login_required
def favourites_add_workout(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    try:
        fav_wo = FavouriteWorkout.objects.get(workout=workout, user=request.user)
        fav_wo.delete()
    except FavouriteWorkout.DoesNotExist:
        new_wo = FavouriteWorkout.objects.create(workout=workout, user=request.user)
        new_wo.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def get_exercises_with_likes(request):
    # KEEP IN MIND ALL THE CHANGES THAT ARE MADE IN THIS MODEL ARE NOT SAVED TO DB
    # ONLY MODIFIED FOR THE FRONT END
    exercise_models = None
    try:
        exercise_models = Exercise.objects.filter(Public=True)
    except Exercise.DoesNotExist:
        return None

    return add_like_information_to_exercises(request, exercise_models)


def add_like_information_to_exercises(request, exercise_models):
    if exercise_models:
        for model in exercise_models:
            model = creation_time_passed(model)
            # Get the count of all likes on current exercise
            try:
                likes = ExerciseRating.objects.filter(Exercise=model, Rating=1).count()
            except ExerciseRating.DoesNotExist:
                likes = 0
            # Get the count of all dislikes on current exercise
            try:
                dislikes = ExerciseRating.objects.filter(Exercise=model, Rating=-1).count()
            except ExerciseRating.DoesNotExist:
                dislikes = 0

            # Edit the values in the model instance (only for front end, not doing a model.save())
            model.Likes = likes
            model.Dislikes = dislikes

            # If the user is logged in we want to show him if he liked something
            if request.user.is_authenticated:
                try:
                    # Trying to fetch a user rating model instance on the current exercise
                    user_rating = ExerciseRating.objects.get(Exercise=model, Judge=request.user)
                except ExerciseRating.DoesNotExist:
                    # Set as none if it cannot be found
                    user_rating = None

                # If the user has rated this exercise
                if user_rating:
                    # If the user liked the exercise
                    if user_rating.Rating == 1:
                        model.Has_Liked = True
                    # If the user disliked the exercise
                    elif user_rating.Rating == -1:
                        model.Has_Disliked = True

            if request.user.is_authenticated:
                try:
                    user_favourite = FavouriteExercise.objects.filter(user=request.user, exercise=model)
                except FavouriteExercise.DoesNotExist:
                    user_favourite = None

                if user_favourite:
                    model.has_favourite = True

        return exercise_models


def get_workouts_with_likes(request):
    workout_models = None
    try:
        workout_models = Workout.objects.filter(Public=True)
    except Workout.DoesNotExist:
        return None
    return add_like_information_to_workouts(request, workout_models)


def add_like_information_to_workouts(request, workout_models):
    if workout_models:
        for model in workout_models:
            model = creation_time_passed(model)
            # Get the count of all likes on current exercise
            try:
                likes = WorkoutRating.objects.filter(Workout=model, Rating=1).count()
            except WorkoutRating.DoesNotExist:
                likes = 0
            # Get the count of all dislikes on current exercise
            try:
                dislikes = WorkoutRating.objects.filter(Workout=model, Rating=-1).count()
            except WorkoutRating.DoesNotExist:
                dislikes = 0

            # Edit the values in the model instance (only for front end, not doing a model.save())
            model.Likes = likes
            model.Dislikes = dislikes

            # If the user is logged in we want to show him if he liked something
            if request.user.is_authenticated:
                try:
                    # Trying to fetch a user rating model instance on the current exercise
                    user_rating = WorkoutRating.objects.get(Workout=model, Judge=request.user)
                except WorkoutRating.DoesNotExist:
                    # Set as none if it cannot be found
                    user_rating = None

                # If the user has rated this exercise
                if user_rating:
                    # If the user liked the exercise
                    if user_rating.Rating == 1:
                        model.Has_Liked = True
                    # If the user disliked the exercise
                    elif user_rating.Rating == -1:
                        model.Has_Disliked = True

                if request.user.is_authenticated:
                    try:
                        user_favourite = FavouriteWorkout.objects.filter(user=request.user, workout=model)
                    except FavouriteWorkout.DoesNotExist:
                        user_favourite = None

                    if user_favourite:
                        model.has_favourite = True

        return workout_models


def creation_time_passed(model):
    date_time_now = datetime.now()
    timezone = pytz.timezone("UCT")
    date_time_now = timezone.localize(date_time_now)
    time_diff = date_time_now - model.CreatedAt
    time_delta = time_diff.total_seconds()
    minutes = time_delta / 60
    time_passed_value = round(minutes)
    time_passed_unit = "min"
    if minutes >= 60:
        hours = minutes / 60
        time_passed_unit = "hours"
        time_passed_value = round(hours)
        if hours >= 24:
            days = hours / 24
            time_passed_unit = "days"
            time_passed_value = round(days)
            if days >= 7:
                weeks = days / 7
                time_passed_unit = "weeks"
                time_passed_value = round(weeks)
                if weeks >= 4:
                    months = weeks / 4
                    time_passed_unit = "months"
                    time_passed_value = round(months)
                    if months >= 12:
                        years = months / 12
                        time_passed_unit = "years"
                        time_passed_value = round(years)

    time_passed_string = '{} {} ago'.format(time_passed_value, time_passed_unit)
    model.time_passed = time_passed_string
    return model
