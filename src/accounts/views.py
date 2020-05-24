from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    """
        Handles the proccess to register a new user
        Renders the signup view and the index if user info
        is valid
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('menu:index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    """
        Handles the proccess to validate an user request
        to login and renders the login view
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('menu:index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
        Logout an user
    """
    if request.method == "POST":
        logout(request)
        return redirect('menu:index')
