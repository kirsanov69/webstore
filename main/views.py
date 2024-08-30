from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category

def index(request):

    category = Category.objects.all()

    context = {
        'title': 'Webstore - главная',
        'content': 'Магазин мебели Roga I Kopyta',
        'category': category
    
}

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Webstore - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин мебели Roga I Kopyta - это лучший магазин мебели во всем мире!'
    
}

    return render(request, 'main/about.html', context)