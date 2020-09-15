from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .forms.create_workout_form import CreateWorkoutForm
from .models import Workout, Exercise


def index(request):
    return HttpResponse ("Example")


def create_workout(request):
    if request.method == 'POST':
        form = CreateWorkoutForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, "workoutapp/templates/createWorkout/create_workout.html", {
            'form': CreateWorkoutForm(), "errors": form.errors
        })

    return render(request, "workoutapp/templates/createWorkout/create_workout.html", {
        'form': CreateWorkoutForm()
    })
    return render(request, "workoutapp/templates/dashboard/dashboard.html", {})
