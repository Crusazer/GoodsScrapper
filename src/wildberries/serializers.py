from rest_framework import serializers


class AddProductSerializer(serializers.Serializer):
    article = serializers.IntegerField(write_only=True)
