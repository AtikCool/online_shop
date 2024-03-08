import uuid
from rest_framework import generics
from django.db.models import Max, Min
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from rest_framework.response import Response

from .serializers import ProductSerializer
# Create your views here.
from rest_framework.views import APIView
from django.core.paginator import Paginator
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import render
from functools import reduce

from main.models import *


# Create your views here.


def cool_profile(request):
    def count_elements(lst):
        return {i: lst.count(i) for i in lst}

    products_id = count_elements(request.session['basket'])
    products = map(lambda x: Product.objects.get(id=x), products_id.keys())

    basket = BasketCool.objects.filter(user=request.session['username'])

    if request.session['basket'] == []:
        total_sum = 0
        total_quantity = 0
    else:
        products_id = count_elements(request.session['basket'])
        products = list(map(lambda x: Product.objects.get(id=x), products_id.keys()))
        basket = BasketCool.objects.filter(user=request.session['username'])
        products = list(zip(products_id, products))
        price_in_id = {}

        for x in products_id:
            if x in price_in_id.keys():
                price_in_id[x] = price_in_id.get(x)+1
            price_in_id[int(Product.objects.get(id=x).price*products_id.get(x))] = x
        total_sum = price_in_id.items()
        total_sum = reduce(lambda x, y: (x[0] * x[1]) + (y[0] * y[1]), list(price_in_id.items()))
        total_quantity = sum(products_id.values())
    return render(request, 'main/basket.html',
                  {'products': products, 'basket': basket, 'total_sum': total_sum, 'total_quantity': total_quantity})

'''def menu(request, slug=None , page=1):

    max_price = Product.objects.aggregate(Max('price', default=0))
    min_price = Product.objects.aggregate(Min('price', default=0))
    price_data = {'min_price':list(min_price.values())[0],'max_price':list(max_price.values())[0] }
    search_value = request.GET.get("search")
    min_pricee = request.GET.get('min_price')
    max_pricee = request.GET.get('max_price')
    query_data = {}
    product = Product.objects.all()
    if max_pricee:
        query_data['max_price'] = max_pricee
        product = product.filter(price__lte=max_pricee)
    if min_pricee:
        query_data['min_price'] = min_pricee
        product = product.filter(price__gte=min_pricee)
    if slug:
        category = Category.objects.get(slug=slug)
        product = product.filter(cat=category)
    if search_value !='' and search_value:
        query_data['search_value'] = search_value
        product = product.filter(name__contains=search_value)

    if request.GET.get('sort_method') == 'up':
        product.order_by('price')
    elif request.GET.get('sort_method') == 'down':
        product.order_by('-price')


    paginator = Paginator(object_list=product, per_page=9)
    products_paginator = paginator.page(page)
    context={'category':Category.objects.all(), 'product': products_paginator, 'price_data':price_data, 'query_data':query_data}

    return render(request, 'main/menu.html', context=context)'''
'''class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer'''
class ProductAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        return Response({'title':"It's a get request", 'product':ProductSerializer(product, many=True).data})
    def post(self, request):
        return Response({'title': "It's a post request"})

class ProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/menu.html'
    def get(self, request, slug=None, page=1):
        max_price = Product.objects.aggregate(Max('price', default=0))
        min_price = Product.objects.aggregate(Min('price', default=0))
        price_data = {'min_price': list(min_price.values())[0], 'max_price': list(max_price.values())[0]}
        search_value = request.GET.get("search")
        min_pricee = request.GET.get('min_price')
        max_pricee = request.GET.get('max_price')
        query_data = {}
        product = Product.objects.all()
        if max_pricee:
            query_data['max_price'] = max_pricee
            product = product.filter(price__lte=max_pricee)
        if min_pricee:
            query_data['min_price'] = min_pricee
            product = product.filter(price__gte=min_pricee)
        if slug:
            category = Category.objects.get(slug=slug)
            product = product.filter(cat=category)
        if search_value != '' and search_value:
            query_data['search_value'] = search_value
            product = product.filter(name__contains=search_value)

        if request.GET.get('sort_method') == 'up':
            product.order_by('price')
        elif request.GET.get('sort_method') == 'down':
            product.order_by('-price')
        product = ProductSerializer(product, many=True).data
        paginator = Paginator(object_list=product, per_page=9)
        products_paginator = paginator.page(page)
        return Response({'category':Category.objects.all(), 'product': products_paginator, 'price_data':price_data, 'query_data':query_data})

def main(request):



    return render(request, 'main/main.html')







def cool_basket_add(request, product_id):
    if 'username' in request.session:
        pass
    else:
        request.session['username'] = str(uuid.uuid4())
    if 'basket' not in request.session:
        request.session['basket'] = []
    basket = request.session['basket']
    del request.session['basket']
    request.session['basket'] = basket + [product_id]


    product = Product.objects.get(id=product_id)
    baskets = BasketCool.objects.filter(user=request.session['username'], product=product)


    if not baskets.exists():
        BasketCool.objects.create(user=request.session['username'], product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def cool_basket_remove(request, basket_id):
    request.session['basket'] = list(filter(lambda x:False if x == basket_id else True,request.session['basket']))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
