from .basket import Basket

# Context processor to provide the user's shopping basket to all templates.
def basket(request):
    return {'basket': Basket(request)}
