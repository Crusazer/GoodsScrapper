from rest_framework import serializers

from wildberries.models import Product


class AddProductSerializer(serializers.Serializer):
    article = serializers.IntegerField(write_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
