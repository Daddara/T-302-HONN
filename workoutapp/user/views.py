from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dashboard.views import dashboard
from wallet.models import Wallet
from workout.models import Exercise
from .forms.create_account_form import CreateAccountForm
from user.models import Follow


# Create your views here.
from .models import UserInfo


def register(request):
    if request.method == 'POST':
        form = CreateAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            new_user = User.objects.get(username=username)
            user_info = UserInfo.objects.create(user=new_user)
            user_info.save()
            wallet = Wallet.objects.create(user=new_user)
            wallet.save()
            return redirect('login')

        return render(request, 'user/register.html', {
            'form': form, "errors": form.errors
        })

    return render(request, 'user/register.html', {
        'form': CreateAccountForm()
    })


@login_required
def profile(request):
    try:
        exercises = Exercise.objects.filter(Creator=request.user)
    except Exercise.DoesNotExist:
        exercises = None
    user_info = UserInfo.objects.get(user=request.user)
    return render(request, 'user/profile.html', context={'user_info': user_info, 'exercises': exercises})



@login_required
def following(request):
    user = Follow.objects.get(Username=request.user)
    context = {'follow': user}
    return render(request, 'user/followerlist.html')

@login_required
def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, Creator=request.user, pk=exercise_id)
    exercise.delete()

    return redirect('profile')