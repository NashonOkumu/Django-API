# urls.py
from django.urls import path
from .views import ProductBulkCreateView

urlpatterns = [
    path('products/bulk-create/', ProductBulkCreateView.as_view(), name='bulk-create'),
]
