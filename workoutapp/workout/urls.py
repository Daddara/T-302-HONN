from django.urls import path
from . import views

urlpatterns = [
    path('workout/create_workout', views.create_workout, name='create workout'),
    path('workout/create_exercise', views.create_exercise, name='create exercise'),

]