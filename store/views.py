from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import Product, Category, User


#categories 

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(Category=category)  
    return render(request, 'store/product/category.html', {'category': category, 'products': products})



#products

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def product_details(request, slug):
    product = get_object_or_404 (Product, slug=slug, in_stock=True)
    return render(request, 'store/product/detail.html', {'product': product})





