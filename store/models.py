from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



#Category details..........
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    
    def get_absolute_url(self):
      return reverse('store:category_list', args=[self.slug])  
    
    class Meta:
            verbose_name_plural = 'categories'   #dunder method to showing the name on the admin panel.....

    def __str__(self):
          return self.name
    

#Product details..........

class Product(models.Model):
      Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
      created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_creator')
      title = models.CharField(max_length= 500)
      author = models.CharField(max_length=255, default= 'author')
      description = models.TextField(blank=True)
      image = models.ImageField(upload_to='images/')
      slug = models.SlugField(max_length=255)
      price = models.DecimalField(max_digits=5, decimal_places=2)
      in_stock =models.BooleanField(default=True)
      is_active = models.BooleanField(default=True)
      created = models.DateTimeField(auto_now_add=True)   # auto now add, will take the date only once at the time of creation.
      updated = models.DateTimeField(auto_now=True)


      def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])


    #dunder method to showing the name on the admin panel.....

      class Meta:
            verbose_name_plural = 'Product'
            ordering = ('-created',)   # the last item added to the db is showing first .....


      def __str__(self):
            return self.title
 