from .models import Category

# Context processor to provide a list of categories to all templates.
def categories(request):
    return {
        'categories': Category.objects.all()
    }
