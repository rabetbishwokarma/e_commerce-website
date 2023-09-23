from django.shortcuts import get_object_or_404, render
from .models import Category, Product, User

# View for displaying a list of products in a specific category.
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(Category=category)  
    return render(request, 'store/product/category.html', {'category': category, 'products': products})

# View for displaying a list of all available products.
def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})

# View for displaying details of a specific product.
def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product/single_product.html', {'product': product})
