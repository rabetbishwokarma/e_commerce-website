from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug= 'django')


    def test_category_models_entry(self):
        """
        Test cateory model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_models_entry(self):
        """
        Test cateory model default name
        """

        data = self.data1
        self.assertEqual(str(data), 'django')

    
class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug= 'django')
        User.objects.create(usernmae= 'admin')
        self.data1 = Product.objects.create(category_id=1, title='django begineers', created_by_id=1,
                    slug = 'django=begineers', price='20.00',image='django.png')


        