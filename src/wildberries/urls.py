from django.urls import path
from .views import AddProductView, ProductListView


urlpatterns = [
    path("products/add/", AddProductView.as_view(), name="add-product"),
    path("products/", ProductListView.as_view(), name="get-products"),
]