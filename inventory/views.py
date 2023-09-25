from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, ProductDetail, Side, Movment
from .serializers import ProductSerializer, ProductDetailSerializer, SideSerializer, MovementSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewset(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer


class SideViewset(viewsets.ModelViewSet):
    queryset = Side.objects.all()
    serializer_class = SideSerializer



class MovmentViewset(viewsets.ModelViewSet):
    queryset = Movment.objects.all()
    serializer_class = MovementSerializer

    def create(self, request):
        move_data = request.data
        product = Product.objects.get(id=move_data['product'])
        sender = Side.objects.get(id=move_data['sender'])
        reciver = Side.objects.get(id=move_data['reciver'])
        new_movment = Movment.objects.create(
            product=product, amount=move_data['amount'], sender=sender, reciver=reciver)
        if reciver.type == "store":
            prod_detail, created = ProductDetail.objects.get_or_create(
                product=product, place=reciver)
            prod_detail.amount += int(move_data['amount'])
            prod_detail.save()

        elif reciver.type == 'port' or reciver.type == 'consumer':
            if sender.type == "store":
                prod_sender, created = ProductDetail.objects.get_or_create(
                    product=product, place=sender)

                prod_sender.amount -= int(move_data['amount'])
                if prod_sender.amount >= 0:
                    prod_sender.save()
                else:
                    return Response("amount not enough", status=status.HTTP_400_BAD_REQUEST)
            if (reciver.type == "port"):
                prod_reciver, created = ProductDetail.objects.get_or_create(
                    product=product, place=reciver)
                prod_reciver.amount += int(move_data['amount'])
                prod_reciver.save()

        new_movment.save()
        serializer = self.serializer_class(new_movment)
        return Response(serializer.data)
