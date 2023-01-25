from django.contrib import admin

from .models import Subject_net, Product, Contact, Provider


class Subject_netAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'products', 'created_date')
    search_fields = ('title', 'contacts', 'products')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_model', 'date_out', 'quantity')
    search_fields = ('product_title', 'date_out')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house')
    search_fields = ('country', 'city')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('providers', 'arrears')
    search_fields = ('providers', 'arrears')


admin.site.register(Subject_net, Subject_netAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Provider, ProviderAdmin)

