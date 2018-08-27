from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    print(request)
    return HttpResponse('Hello! The Current server time is {now}'.format(
        now=datetime.now().strftime('%d/%m/%Y - %H:%M hours')
    ))

def trace(request):
    """request methods"""
    """ ; to define 2 operations in a single line """
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')
