from django.test import TestCase
from restaurant.models import Menu
import unittest

class MenuTest(unittest.TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item, 'IceCream : 80')



