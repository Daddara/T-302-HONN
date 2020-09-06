from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path('accounts/profile/', views.placeholder_home, name='profile'),
    path('', views.placeholder_home, name='placeholder_home'),
]