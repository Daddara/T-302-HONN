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


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            new_user = User.objects.get(username=username)
            wallet = Wallet.objects.create(user=new_user)
            wallet.save()
            return redirect('login')

        return render(request, 'user/register.html', {
            'form': form, "errors": form.errors
        })

    return render(request, 'user/register.html', {
        'form': CreateAccountForm()
    })

def profile(request):
    return redirect('dashboard')


#@login_required
def following(request):
    #user = Follow.objects.get(Username=request.user)
    #context = {'follow': user}
    return render(request, 'user/followerlist.html')

def profile(request):
    return redirect('dashboard')

