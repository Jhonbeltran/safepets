""" User Forms """
from django import forms

class ProfileForm(forms.Form):
    """ We use required to be consistent with the middlware"""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
