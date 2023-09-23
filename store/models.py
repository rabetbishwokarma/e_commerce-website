from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# ProductManager is used to manage products
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

# Category details
class Category(models.Model):
    """
    This model represents product categories.
    """

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])  # URL for viewing the list of products in this category
    
    class Meta:
        verbose_name_plural = 'categories'  # Display name for categories on the admin panel

    def __str__(self):
        return self.name

# Product details
class Product(models.Model):
    """
    This model represents individual products.
    """

    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=255, default='author')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpeg')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # Date of creation
    updated = models.DateTimeField(auto_now=True)  # Date of last update
    objects = models.Manager()
    products = ProductManager()  # Custom manager for active products only

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])  # URL for viewing the product details

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created',)  # Ordering products by creation date (latest first)

    def __str__(self):
        return self.title  # Display product title in admin panel
