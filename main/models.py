from django.db import models
from django.urls import reverse



class Product(models.Model):
    name = models.CharField(max_length=45)
    anons = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    slug = models.SlugField(max_length=125, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'post_slug' : self.slug})
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45, verbose_name='Category name')
    slug = models.SlugField(max_length=125)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return f'/menu/category/{self.slug}'
class BasketQuerySet(models.QuerySet):
    def total_sum(self):

        return sum(x.sum() for x in self)

    def total_quantity(self):


        return sum(x.quantity for x in self)



class BasketCool(models.Model):
    user = models.CharField(max_length=200)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='cool_product')
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestam = models.DateTimeField(auto_now_add=True)
    #objects = BasketQuerySet.as_manager()


    def sum(self):
        return self.product.price * self.quantity
    def get_absolute_url(self):
        return f'/menu/category/{self.slug}'


