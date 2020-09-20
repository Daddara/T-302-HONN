from django.urls import path
from . import views

urlpatterns = [
    path('', views.placeholder_home, name='placeholder_home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('public/workouts/', views.workouts, name='public_workouts'),
    path('public/exercises/', views.exercises, name='public_exercises'),
]