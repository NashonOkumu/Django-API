from django.test import TestCase
from django.urls import reverse
import json

class ProductAPITest(TestCase):
    def test_bulk_create_product(self):
        url = reverse('bulk-create')
        data = {
            "name": "Yoghurt",
            "image": "yoghurt.jpg",
            "variants": [
                {
                    "sku": "yoghurt-vanilla",
                    "name": "Vanilla",
                    "price": "2.99",
                    "details": "Vanilla flavored yoghurt"
                },
                {
                    "sku": "yoghurt-strawberry",
                    "name": "Strawberry",
                    "price": "2.99",
                    "details": "Strawberry flavored yoghurt"
                }
            ]
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
