from django.urls import path

from . import views

urlpatterns = [
    path('event', views.log_frontend_event, name='log_frontend_event'),
]
