from django.urls import path
from . import views

urlpatterns = [
    path('create_workout', views.create_workout, name='create workout'),
    path('create_exercise', views.create_exercise, name='create exercise'),
    path('rate_exercise', views.rate_exercise, name='rate_exercise'),
    path('add_exercises/<int:workout_id>/', views.add_exercises, name='add exercises'),
    path('rate_workout', views.rate_workout, name='rate_workout'),
    path('exercise_details/<int:exercise_id>/', views.exercise_details, name='exercise_details'),
    path('update_exercise/<int:exercise_id>/', views.update_exercise, name='update_exercise'),
    path('workout_details/<int:workout_id>/', views.workout_details, name='workout_details'),
    path('delete-exercise/<int:exercise_id>/', views.delete_exercise, name="delete-exercise"),
    path('delete-workout/<int:workout_id>/', views.delete_workout, name="delete-workout"),
    path('workout_details/<int:workout_id>/remove-exercise/<int:exercise_id>/', views.remove_exercise,
         name='remove-workout-exercise'),
    path('all-exercises-json/', views.get_all_exercises_json, name="get-all-exercises"),
    path('workout_details/<int:workout_id>/add-exercise-to-workout/<int:exercise_id>/<int:unit_id>/<int:amount>/',
         views.add_exercise_to_workout, name='add-exercise-to-workout')
]
#http://127.0.0.1:8000/workout/workout-details/1/add-exercise-to-workout/2/1/1/
#http://127.0.0.1:8000/workout/workout-details/1/add-exercise-to-workout/1/1/1/