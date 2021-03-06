from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import UserInfo


class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class EditUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['user', 'slug', 'friends']
        widgets = {
            'birth_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }







