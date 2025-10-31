from django.test import TestCase
from .models import FoodItem

class FoodItemModelTest(TestCase):
    def test_create_food_item(self):
        item = FoodItem.objects.create(name='Apple', calories=95)
        self.assertEqual(str(item), 'Apple (95 kcal)')
