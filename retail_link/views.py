from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Contact, Product, Subject_net, Provider
from .serializers import ContactSerializer, ContactListSerializer, ProductListSerializer, ProductSerializer, Subject_netCreateSerializer, Subject_netSerializer, ContactCreateSerializer, ProductCreateSerializer, ProviderCreateSerializer, ProviderSerializer, ProviderListSerializer


class ContactCreateView(generics.CreateAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactCreateSerializer


class ContactView(RetrieveUpdateDestroyAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactListView(generics.ListAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['country']


class ProductCreateView(generics.CreateAPIView):
    model = Product
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCreateSerializer


class ProductListView(generics.ListAPIView):
    model = Product
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProviderCreateView(generics.CreateAPIView):
    model = Provider
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCreateSerializer


class ProviderListView(generics.ListAPIView):
    model = Provider
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProviderListSerializer
    pagination_class = LimitOffsetPagination


class ProviderView(generics.RetrieveUpdateDestroyAPIView):
    model = Provider
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


class Subject_netCreateView(generics.CreateAPIView):
    model = Subject_net
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Subject_netCreateSerializer


class Subject_netListView(generics.ListAPIView):
    model = Subject_net
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Subject_netSerializer


class Subject_netView(generics.RetrieveUpdateDestroyAPIView):
    model = Subject_net
    serializer_class = Subject_netSerializer
    permission_classes = [permissions.IsAuthenticated]


