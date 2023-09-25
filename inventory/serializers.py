from rest_framework import serializers
from . import models


class ProductDetailProductSerializer (serializers.ModelSerializer):

    place_name = serializers.CharField(source='place.name', read_only=True)

    class Meta:
        model = models.ProductDetail
        fields = ['place_name', 'amount']


class ProductDetailSerializer (serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)
    place_name = serializers.CharField(source='place.name', read_only=True)

    class Meta:
        model = models.ProductDetail
        fields = ['id', 'product', 'product_name',
                  'place', 'place_name', 'amount']


class ProductDetailSideSerializer (serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = models.ProductDetail
        fields = ['product_name', 'amount']


class MovementSerializer (serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    sender_name = serializers.CharField(source='sender.name', read_only=True)
    reciver_name = serializers.CharField(source='reciver.name', read_only=True)

    class Meta:
        model = models.Movment
        fields = ['id', 'product_name', 'product', 'amount',
                  'sender', 'reciver', 'sender_name', 'reciver_name']


class SideSerializer(serializers.ModelSerializer):
    send = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    recive = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    detail = ProductDetailSideSerializer(many=True, read_only=True)

    class Meta:
        model = models.Side
        fields = ['id', "name", 'type', 'recive', "send", 'detail']


class ProductSerializer (serializers.ModelSerializer):
    detail = ProductDetailProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'detail']
