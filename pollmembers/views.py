from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signout(request):
    logout(request)
    return reverse_lazy('home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() # save the user

            # login this new user
            user_name = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username = user_name, password = password)
            login_user(request, user)
            return reverse_lazy('home')

        else:
            # form not valid
            return render(request, 'auth/signup.html', {'form': form })

    else:
        # not post = GET
        form = UserCreationForm()
        return render(request, 'auth/signup.html', {'form': form })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        # validate credential
        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = user_name, password = password)

        if user is not None: 
            # valid creds
            login_user(request, user) # save the user as logged in
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, "auth/login.html", {"form": form})

    else:
        form = AuthenticationForm()
        return render(request, "auth/login.html", {"form": form})   


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'
