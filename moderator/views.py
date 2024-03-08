from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.forms import ProductChangeForm, ProductForm
from main.models import Product

@staff_member_required()
def product_add(request):
    if request.methogitd == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:menu'))
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request,'admin/products_add.html', context)
@staff_member_required()
def admin_product_list(request):
    product = Product.objects.all()
    return render(request=request, template_name='admin/products_list.html', context={'product': product})
@staff_member_required()
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductChangeForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('moder:admin_product_list'))
    else:
        form = ProductChangeForm(instance=Product.objects.get(id=product_id))


    return render(request, 'admin/update_product.html', {'form': form, 'product': product})
# Create your views here.
