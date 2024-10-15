from django.urls import path
from .views import AddProductView


urlpatterns = [
    path("products/add/", AddProductView.as_view(), name="add-product"),
]