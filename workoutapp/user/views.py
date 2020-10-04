from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dashboard.views import dashboard
from wallet.models import Wallet
from .forms.create_account_form import CreateAccountForm
from user.models import Follow
from workout.models import Exercise


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
    try:
        poster = Follow.objects.filter(Username=request.user)
    except Follow.DoesNotExist:
        return render(request, 'user/followerlist.html')
    if poster:
        return render(request, 'user/followerlist.html', context={'follow': poster})


@login_required
def searchbarUsers(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = User.objects.all().filter(username=search)
        if post:
            return render(request, 'user/searchResults.html', context={'sr_user': post})

    if request.method == 'POST':
        search = request.GET.get('search')
        post = User.objects.all().filter(username=search)
        poster = post.get(username=search)
        current_user = User.objects.get(username=request.user)
        follow = Follow(Username=current_user, Following=poster, FollowedAt="")
        follow.save()
        return redirect(following)
