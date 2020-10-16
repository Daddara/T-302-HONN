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
]