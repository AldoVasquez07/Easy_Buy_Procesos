from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Agregar búsqueda por nombre
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Paginación
    paginator = Paginator(products, 12)  # Muestra 12 productos por página
    page_number = request.GET.get('page')  # Obtiene el número de página de la URL
    try:
        products = paginator.page(page_number)  # Obtiene la página solicitada
    except PageNotAnInteger:
        products = paginator.page(1)  # Si el número de página no es un entero, muestra la primera página
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Si la página está fuera de rango, muestra la última página

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'query': query})  # Pasar el query al template


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
