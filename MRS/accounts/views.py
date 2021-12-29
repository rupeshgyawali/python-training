from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

# Create your views here.
def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movies:index')
            else:
                form.add_error(None, 'Invalid Credentials')

    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'accounts/register.html', {'form': form})

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('movies:index')