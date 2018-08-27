from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

def hello_world(request):
    print(request)
    return HttpResponse('Hello! The Current server time is {now}'.format(
        now=datetime.now().strftime('%d/%m/%Y - %H:%M hours')
    ))

def trace(request):
    """request methods"""
    """ ; to define 2 operations in a single line """
    """ use c to close the pdb """
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')

def sort_numbers(request):
    """ http://localhost:8000/numbers/?numbers=10,4,5,37 """
    values = request.GET['numbers'].split(',')
    #numbers = list(map(lambda x: int(x), values))
    numbers = [int(i) for i in values]
    numbers_sort = sorted(numbers)
    #numbers_dict = {i: numbers_sort[i] for i in range(len(numbers_sort))}
    #return JsonResponse(numbers_dict)
    numbers_sort = {
        'status': 'ok',
        'numbers': {i: numbers_sort[i] for i in range(len(numbers_sort))},
        'message': 'Integers sorted Succesfuully'
    }
    return HttpResponse(json.dumps(numbers_sort, indent=4),
                        content_type='application/json')

def hi(request, name, age):
    if age < 12:
        message = "Sorry {}, you're not old enough to login".format(name)
    else:
        message = "Hi {}! Welcome to SafePets".format(name)
    return HttpResponse(message)
