from django.urls import path
from . import views

#app name for namespacing URLs.
app_name = 'basket'

urlpatterns = [

    path('', views.basket_summary, name='basket_summary'),  # URL for viewing the basket summary.
    path('add/', views.basket_add, name='basket_add'),  # URL for adding products to the basket.
    path('delete/', views.basket_delete, name='basket_delete'),  # URL for deleting products from the basket.
    path('update/', views.basket_update, name='basket_update'),  # URL for updating the basket.
]
