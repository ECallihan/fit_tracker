from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(
                request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return render(request, 'home.html', {})

    form = CustomUserCreationForm
    return render(request, 'registration/signup.html', {'form': form})
