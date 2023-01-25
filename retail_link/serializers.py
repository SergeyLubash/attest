from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contact, Product, Subject_net, Provider
from core.models import User
from core.serializers import UserSerializer

USER_MODEL = get_user_model()


class ContactCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        read_only_fields = ('id', 'email', 'country', 'city', 'street', 'house')
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('id', 'country', 'city')


class ProductCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        read_only_fields = ('id', 'product_title', 'product_model', 'date_out', 'quantity')
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'product_title', 'product_model', 'date_out', 'quantity')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'product_title', 'quantity')


class ProviderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Provider
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'


class ProviderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class Subject_netCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subject_net
        read_only_fields = ('id', 'title', 'contacts', 'products', 'created_date')
        fields = '__all__'


class Subject_netSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subject_net
        fields = '__all__'
        read_only_fields = ('id', 'title', 'contacts', 'products', 'created_date')


class Subject_netListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('id', 'title')
