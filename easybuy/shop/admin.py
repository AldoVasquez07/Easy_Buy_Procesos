from django.contrib import admin
from .models import Category, Product, Offer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['motive', 'slug', 'discount']
    list_editable = ['discount']
    prepopulated_fields = {'slug': ('motive',)}




