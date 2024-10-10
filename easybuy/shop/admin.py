from django.contrib import admin
from .models import Category, Product, Oferta

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


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ['motivo', 'slug', 'descripcion', 'descuento']
    list_editable = ['descripcion', 'descuento']
    prepopulated_fields = {'slug': ('motivo',)}




