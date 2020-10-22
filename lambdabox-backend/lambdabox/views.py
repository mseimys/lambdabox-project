from django.contrib.auth import get_user_model
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")


def login(request):
    User = get_user_model()
    user, created = User.objects.get_or_create(username="user")
    user.set_password("user")
    user.save()
    user_login(request, user)
    return redirect("/")


def logout(request):
    user_logout(request)
    return redirect("/")
