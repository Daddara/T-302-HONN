from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('profile/update', views.edit_profile_view, name='edit-user'),
    path('profile/<slug:slug>', views.profile_view, name='profile'),
    path('following/', views.following, name='following'),
    path('delete-exercise/<int:exercise_id>/', views.delete_exercise, name="delete-exercise"),
    path('delete-workout/<int:workout_id>/', views.delete_workout, name="delete-workout"),
    path('searchbarUsers/', views.searchbarUsers, name='searchbarUsers'),
    path('friends/', views.view_friend_and_requests, name='user_friends'),

    path('friend-request/send/<int:id>', views.new_friend_request, name='send-request'),
    path('friend-request/cancel/<int:id>', views.cancel_friend_request, name='cancel-request'),
    path('friend-request/delete/<int:id>', views.delete_friend_request, name='delete-request'),
    path('friend-request/accept/<int:id>', views.accept_friend_request, name='accept-request')
]