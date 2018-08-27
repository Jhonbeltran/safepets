from django.http import HttpResponse, JsonResponse
from datetime import datetime

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
    numbers = list(map(lambda x: int(x), values))
    numbers_sort = sorted(numbers)
    numbers_dict = {i: numbers_sort[i] for i in range(len(numbers_sort))}
    return JsonResponse(numbers_dict)
