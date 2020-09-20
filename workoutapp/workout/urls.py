from django.urls import path
from . import views

urlpatterns = [
    path('create_workout', views.create_workout, name='create workout'),
    path('create_exercise', views.create_exercise, name='create exercise'),

]