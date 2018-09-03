from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm


def update_profile(request):
    """ Update a user's profile view """
    #request.user is provided for a middleware auth
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.biography = data['biography']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request = request,
        template_name= 'users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form':form
        }
    )

# Create your views here.
def login_view(request):
    """ Login User """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def signup(request):
    """ Sign Up Users """
    if request.method == 'POST':
        username = request.POST['username']

        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': "Passwords doesn't match"})

        try:
            """ Here we create the user just with the username and password,
            as we create in the basic admin """
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': "Username is already taken"})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        phone_number = request.POST['phone_number']

        profile = Profile.objects.create(user=user, phone_number=phone_number)

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
