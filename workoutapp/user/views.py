from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms.create_account_form import CreateAccountForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'user/register.html', {
            'form': CreateAccountForm(), "errors": form.errors
        })

    return render(request, 'user/register.html', {
            'form': CreateAccountForm()
        })

def placeholder_home(request):
    return render(request, 'user/placeholder_page.html')