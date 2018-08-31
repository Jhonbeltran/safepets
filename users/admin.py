from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Setup for the profile model Admin """

    """Columns that the admin show"""
    list_display = ('pk', 'user', 'phone_number','website', 'picture')
    """Columns with link to detail view"""
    list_display_links = ('pk', 'user',)
    """Fields editables into de columns"""
    list_editable = ('phone_number', 'website', 'picture')
