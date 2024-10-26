from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            payment_status = True

            if payment_status:
                cart.clear()
                return redirect('orders:order_created')
            else:
                form.add_error(None, "There was a problem with the payment. Please try again.")
    else:
        form = OrderCreateForm()
    
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_created(request):
    order = Order.objects.order_by('-id').first()
    return render(request, 'orders/order/created.html', {'order': order})


def consult_orders(request):
    orders = Order.objects.all()

    query = request.GET.get('q')

    if query:
        orders = orders.filter(email__icontains=query)

    paginator = Paginator(orders, 12)
    page_number = request.GET.get('page')
    try:
        orders = paginator.page(page_number)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request,
                  'orders/order/list.html',
                  {'orders': orders,
                   'query': query})


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'orders/order/detail.html', {'order': order})
