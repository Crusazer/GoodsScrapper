from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddProductSerializer
from .tasks import add_product


# Create your views here.
class AddProductView(APIView):
    serializer_class = AddProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        article: int = serializer.validated_data['article']
        add_product.delay(article)
        return Response(status=status.HTTP_201_CREATED)
