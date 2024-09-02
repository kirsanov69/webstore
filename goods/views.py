from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_list_or_404, render

from goods.models import Product

# Create your views here.
def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = Product.objects.all()

    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
        # if not goods.exists():
        #     raise Http404(f'Категория "{category_slug}" не найдена')
        
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Каталог товаров",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)