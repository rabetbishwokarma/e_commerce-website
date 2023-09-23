from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


@skip("demonstarting skipping)")
class Testskip(TestCase):
    def test_skip(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c =Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='personal development', slug= 'django')
        Product.objects.create(category_id =1, title='48 laws of power', created_by_id=1,
                               slug='48 laws of power ', price='20.00', image='48 laws')


    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST = 'noaddress.com')
        self.assertEqual(response.status_code,400)
        rseponse = self.cases.get('/', HTTP_HOST ='yourdomain.com')
        self.assertEqual(rseponse.status_code, 200)

    # def test_homepage_url(self):