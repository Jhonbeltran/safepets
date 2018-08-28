#from django.shortcuts import render
from django.http import HttpResponse
# Utilities
from datetime import datetime

posts = [
    {
        'name': 'title',
        'user': 'username',
        'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%M hours'),
        'picture': 'https://picsum.photos/200/300?image=1083',
    },
    {
        'name': 'title',
        'user': 'username',
        'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%M hours'),
        'picture': 'https://picsum.photos/200/300/?random',
    },
    {
        'name': 'title',
        'user': 'username',
        'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%M hours'),
        'picture': 'https://picsum.photos/200/300?image=1080',
    },
    {
        'name': 'title',
        'user': 'username',
        'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%M hours'),
        'picture': 'https://picsum.photos/200/300?image=1050',
    },
]

def list_posts(request):
    """ Code generate like script CGI """
    content = []
    for post in posts:
        #Desempaquetamos el diccionario usando **
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - {timestamp}</small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
