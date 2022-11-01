from django.shortcuts import render
from rest_framework import generics, permissions, pagination
from rest_framework.permissions import IsAuthenticated

from .serializers import VendorSerializer, VendorDetailSerializer, ProductListSerializer, ProductDetailSerializer, \
    CustomerDetailSerializer, CustomerListSerializer, OrderSerializer,  OrderDetailSerializer
from .models import Vendor, Product, Customer, Order, OrderItems


# Vendor serializer.
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer


# Product serializer
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = pagination.PageNumberPagination


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# Customer serializer
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


# Order serializer
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.ListAPIView):
    # queryset = OrderItems.objects.all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_items = OrderItems.objects.filter(order=order)

        return order_items
