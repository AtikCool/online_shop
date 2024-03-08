from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'anons', 'status', 'image', 'price', 'slug', 'cat_id',)
    '''id = serializers.IntegerField()
    name = serializers.CharField(max_length=45)
    anons = serializers.CharField(max_length=150)
    status = serializers.BooleanField(default=True)
    image = serializers.ImageField(use_url='images/')
    price = serializers.DecimalField(max_digits=10, decimal_places=0)
    slug = serializers.SlugField(max_length=125)
    cat_id = serializers.IntegerField()'''