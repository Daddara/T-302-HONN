from django.urls import path
from . import views

urlpatterns = [
    path('create_workout', views.create_workout, name='create workout'),
    path('create_exercise', views.create_exercise, name='create exercise'),
    path('add_exercises', views.add_exercises, name='add exercises'),
    path('rate_exercise', views.rate_exercise, name='rate_exercise'),
    path('add_exercises/<int:workout_id>/', views.add_exercises, name='add exercises'),
    path('rate_workout', views.rate_workout, name='rate_workout'),
    path('exercise_details/<int:exercise_id>', views.exercise_details, name='exercise_details'),
]