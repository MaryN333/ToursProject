from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm  # <- NEW!!!
from .forms import UserCreateForm  # <- NEW!!!
from django.contrib.auth.forms import AuthenticationForm  # <- NEW!!!
from django.contrib.auth import login, logout, authenticate  # <- NEW!!!
from django.contrib.auth.decorators import login_required

# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:  # <- NEW!!!
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('shop:index')
            except IntegrityError:  # <- NEW!!!
                return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm, 'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('shop:index')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('shop:index')
