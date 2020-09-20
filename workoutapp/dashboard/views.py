from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from workout.models import Workout, Exercise
from django.contrib.auth.decorators import login_required

# Create your views here.
def placeholder_home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'user/placeholder_page.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def workouts(request):
    context = {'workouts': Workout.objects.filter(Public=True)}
    return render(request, 'dashboard/public_workouts.html', context)

def exercises(request):
    context = {'exercises': Exercise.objects.filter(Public=True)}
    return render(request, 'dashboard/public_exercises.html', context)