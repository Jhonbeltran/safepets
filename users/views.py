from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    """ Login User """
    return render(request, 'users/login.html')
