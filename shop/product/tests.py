import unittest

from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
import datetime


class ProductUnauthTests(APITestCase):

    def setUp(self) -> None:
        p = Product(title="Toy", price=200, category="Toys", description="Puppet")
        p.save()


    def test_list_product(self):
        """
        Test to list all the persons in the list
        """

        url = 'https://127.0.0.1:8000/products/'
        response = self.client.get(url, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json), 4)

    @unittest.expectedFailure
    def test_create_product(self):
        """
        Tests creating a new person object
        """
        # self.client.login(username='admin', password='admin')
        url = 'https://127.0.0.1:8000/products/'
        data = {
            'title': 'Hat',
            'price': 169,
            'category': 'Clothes',
            'description': 'red'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        p = Product.objects.get(title='Hat')
        self.assertEqual(Product.objects.count(), 10002)
        self.assertEqual(p.title, 'Hat')
        self.assertEqual(p.price, 169)
        self.assertEqual(p.category, 'Clothes')

    @unittest.expectedFailure
    def test_put_product(self):
        """
        Test to see if put works
        """
        p = Product.objects.get(title='Toy')
        url = 'https://127.0.0.1:8000/products/'+str(p.id)+'/'

        data = {
            'title': 'Toy',
            'price': 100,
            'category': 'Toys',
            'description': 'For girls'
        }

        response = self.client.put(url, data, format='json')
        json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        p = Product.objects.get(id=p.id)
        self.assertEqual(p.title, 'Toy')
        self.assertEqual(p.price, 100)

    def test_delete_product(self):
        """
        Test to see if deleting works
        """
        p = Product.objects.get(title='Toy')
        url = 'https://127.0.0.1:8000/products/'+str(p.id)+'/'
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProductAuthTests(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', password='admin')
        self.client.force_authenticate(user)
        p = Product(title="Ball", price=63, category="Sport", description="Football")
        p.save()

    def test_list(self):
        """
        Test to list all the persons in the list
        """

        url = 'https://127.0.0.1:8000/products/'
        response = self.client.get(url, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json), 4)

    def test_create(self):
        """
        Tests creating a new person object
        """
        # self.client.login(username='admin', password='admin')
        url = 'https://127.0.0.1:8000/products/'
        data = {
            'title': 'Laptop',
            'price': 1265,
            'category': 'Electronics',
            'description': 'For games'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        p = Product.objects.get(title='Laptop')
        self.assertEqual(Product.objects.count(), 10002)
        self.assertEqual(p.title, 'Laptop')
        self.assertEqual(p.price, 1265)
        self.assertEqual(p.category, 'Electronics')

    def test_put(self):
        """
        Test to see if put works
        """

        p = Product.objects.get(title='Ball')
        url = 'https://127.0.0.1:8000/products/'+str(p.id)+'/'

        data = {
            'title': 'Ball',
            'price': 90,
            'category': 'Sport',
            'description': 'Basketball'
        }

        response = self.client.put(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)

        p = Product.objects.get(id=p.id)
        self.assertEqual(p.title, 'Ball')
        self.assertEqual(p.price, 90)

    def test_delete(self):
        """
        Test to see if deleting works
        """
        p = Product.objects.get(title='Ball')
        url = 'https://127.0.0.1:8000/products/'+str(p.id)+'/'
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



