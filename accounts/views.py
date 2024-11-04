from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request, 'accounts/signup.html', {'form': form})  # Replace 'home' with the desired redirect view
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request, 'accounts/signin.html', {'form': form})
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

# Create your views here.
