from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from user.models import Follow
from wallet.models import Wallet
from .forms.create_account_form import CreateAccountForm


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


def placeholder_home(request):
    return render(request, 'user/placeholder_page.html')

def following(request):
    context = {'follow': Follow.objects.all()}
    return render(request, 'user/followerlist.html', context)