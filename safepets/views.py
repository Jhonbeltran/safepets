from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse('Hello! The Current server time is {now}'.format(
        now=datetime.now().strftime('%d/%m/%Y - %H:%M hours')
    ))
