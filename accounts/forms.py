from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """
    This form is used to create new users.
    """
    class Meta:
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    """
    This form is used to alter user data.
    """
    class Meta:
        model = User
        fields = ('username',)
