from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/public-workouts/', views.workouts, name='public_workouts'),
    path('dashboard/public-exercises/', views.exercises, name='public_exercises'),
    path('dashboard/my-workouts/', views.user_workouts, name="user_workouts"),
    path('dashboard/my-exercises/', views.user_exercises, name="user_exercises"),
    path('dashboard/public-workouts/filter-category/<int:category_id>/', views.filter_wo_public, name="public-filter-w"),
    path('dashboard/public-exercises/filter-category/<int:muscle_group>/', views.filter_ex_public, name="public-filter-e"),
    path('dashboard/favourite_exercise/', views.favourite_exercise, name='favourite_exercise'),
    path('dashboard/favourite_workout/', views.favourite_workout, name='favourite_workout'),
    path('dashboard/favourites_add_exercise/<int:exercise_id>/', views.favourites_add_exercise, name='favourites_add_exercise'),
    path('dashboard/favourites_add_workout/<int:workout_id>/', views.favourites_add_workout,
         name='favourites_add_workout'),
]