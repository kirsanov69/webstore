from django import db
from django.db import models

from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return round(sum([cart.product_price() for cart in self]), 2)
    
    def total_quantity(self):
        if self:
            return sum([cart.quantity for cart in self])
        return 0


class Cart(models.Model):
    """
    В БД хранятся данные о корзине пользователя, для каждого пользователя может быть несколько товаров,
    соответственно, может быть несколько корзин для каждого пользователя, в которых будетотолько по 1 товару
    Это удобно при аналитике.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')    
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')   
 
    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = CartQueryset().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
    
    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'