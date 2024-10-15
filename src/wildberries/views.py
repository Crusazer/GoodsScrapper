from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product
from .serializers import AddProductSerializer, ProductSerializer
from .tasks import add_product


class AddProductView(CreateAPIView):
    """ Create or update a product by an article """
    serializer_class = AddProductSerializer

    def perform_create(self, serializer):
        article: int = serializer.validated_data['article']
        add_product.delay(article)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
