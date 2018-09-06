"""Safepets middleware catalog. """

from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware

    Ensure every user that is interacting with the platform
    have their profile picture and bio
    """

    def __init__(self, get_response):
        """ middleware initialization. """
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    reverse_update_profile = reverse('users:update_profile')
                    reverse_logout = reverse('users:logout')
                    if request.path not in [reverse_update_profile, reverse_logout]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response
