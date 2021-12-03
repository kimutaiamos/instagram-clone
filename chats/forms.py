from django  import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Image, Profile, Comments


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='required')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
