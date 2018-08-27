from django.http import HttpResponse

def hello_wold(request):
    return HttpResponse('Hello world!')
