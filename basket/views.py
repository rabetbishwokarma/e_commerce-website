from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product
from .basket import Basket

# This function renders the basket summary page.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})

# This function handles adding products to the basket.
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        
        # Get the product object or return a 404 error if not found.
        product = get_object_or_404(Product, id=product_id)
        
        # Add the selected product to the basket with the specified quantity.
        basket.add(product=product, qty=product_qty)

        # Get the updated basket quantity.
        basketqty = basket.__len__()

        # Create a JSON response with the updated basket quantity.
        response = JsonResponse({'qty': basketqty})
        return response

# This function handles deleting products from the basket.
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        
        # Delete the specified product from the basket.
        basket.delete(product=product_id)

        # Get the updated basket quantity and total price.
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        # Create a JSON response with the updated basket quantity and total price.
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

# This function handles updating the quantity of products in the basket.
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        
        # Update the quantity of the specified product in the basket.
        basket.update(product=product_id, qty=product_qty)

        # Get the updated basket quantity and total price.
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        # Create a JSON response with the updated basket quantity and total price.
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
