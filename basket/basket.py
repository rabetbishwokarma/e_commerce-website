from decimal import Decimal
from store.models import Product

class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overridden, as necessary.
    """

    def __init__(self, request):
        # Initialize the Basket instance with the user's session.
        self.session = request.session

        # Retrieve the existing basket data from the session or create an empty one.
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the user's basket session data
        """
        product_id = str(product.id)

        # Check if the product is already in the basket, and update the quantity if it is.
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            # If the product is not in the basket, add a new entry with its price and quantity.
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        # Save the updated basket data.
        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        # Get the product IDs from the basket.
        product_ids = self.basket.keys()

        # Query the database to retrieve the corresponding products.
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            # Associate each product with its entry in the basket.
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            # Convert the price to Decimal and calculate the total price for each item.
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        # Calculate and return the total quantity of items in the basket.
        return sum(item['qty'] for item in self.basket.values())

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            # Update the quantity of a specific product in the basket.
            self.basket[product_id]['qty'] = qty
        # Save the updated basket data.
        self.save()

    def get_total_price(self):
        # Calculate and return the total price of all items in the basket.
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            # Remove a specific product from the basket.
            del self.basket[product_id]

            # Save the updated basket data.
            self.save()

# The save method is used to indicate that changes have been made to the session.
    def save(self):
        self.session.modified = True
