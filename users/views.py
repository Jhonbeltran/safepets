from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm, SignupForm

# Models

from django.contrib.auth.models import User
from posts.models import Post

class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context. """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    """ Users sign up view """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ save form data """
        form.save()
        return super().form_valid(form)

@login_required
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

            url = reverse('users:detail', kwargs={'username':request.user.username})
            return redirect(url)
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
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
