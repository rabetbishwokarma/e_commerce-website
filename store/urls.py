from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_all, name='product_all'),
    path('<slug:slug>/', views.product_details, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),



]

