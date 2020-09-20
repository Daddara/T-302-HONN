from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_workout, name='create workout'),
    path('', views.create_exercise, name='create exercise'),

]