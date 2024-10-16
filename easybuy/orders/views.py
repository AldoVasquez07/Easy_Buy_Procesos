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

            payment_status = True #VALIDANDO PAGO

            if payment_status:
                cart.clear()
                return redirect('orders:order_created')
            else:
                # Si el pago falla, muestra un mensaje de error
                form.add_error(None, "There was a problem with the payment. Please try again.")
    else:
        form = OrderCreateForm()
    
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_created(request):
    order = Order.objects.order_by('-id').first()
    return render(request, 'orders/order/created.html', {'order': order})
