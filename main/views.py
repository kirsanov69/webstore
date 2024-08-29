from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
    'title': 'Webstore',
    'content': 'Welcome to the webstore',
    'list': ['item1', 'item2', 'item3'],
    'dict': {'item1': 1, 'item2': 2},
    'is_authenticated': False,
}

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("Hello, world. You're at the main about.")