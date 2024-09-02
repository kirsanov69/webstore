from django.http import Http404
from django.shortcuts import render

from goods.models import Product

# Create your views here.
def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Product.objects.all()

    else:
        goods = Product.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404(f'Категория "{category_slug}" не найдена')

    context = {
        "title": "Каталог товаров",
        "goods": goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)