from django.shortcuts import render, redirect
from carts.models import CartItem
from django.http import JsonResponse
from .forms import OrderForm
from .models import Order, Payment, OrderProduct
from store.models import Product
import datetime
import os
from .checkday import delivery_day
from email.mime.image import MIMEImage

import json
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, EmailMultiAlternatives
import holidays as hol



def payments(request):
    body = json.loads(request.body)

    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])

    payment = Payment(
        user= request.user,
        payment_id= body['orderTrans'],
        payment_method=body['payments_method'],
        status=body['status'],
        amount_paid=order.order_total,


    )
    
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()
    subtotal = 0
    cart_item_ = CartItem.objects.filter(user = request.user)

    for item in cart_item_:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.price
        orderproduct.ordered = True
        subtotal += item.quantity * item.product.price
        orderproduct.save()

        cart_item = CartItem.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id = orderproduct.id)
        orderproduct.variations.set(product_variation)
 
        orderproduct.save()

        # Reduce the quantity of the sold products
        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()

    # Clear cart
    CartItem.objects.filter(user=request.user).delete() 
    mail_subject = 'Tvoje objednavka'
    message = render_to_string('orders/order_recieved_email.html', {
                'user': request.user,
                'order': order
            })            
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id
    }
    #order = Order.objects.get(user=request.user, is_ordered=True, order_number=body['orderID'])
    ordered_products = OrderProduct.objects.filter(order_id = order.id)
    current_site = get_current_site(request)
    
    context_ = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'payment': payment,
            'subtotal': subtotal,
            'domain': current_site
            }
    d = Context( context_)    
    txtmes = get_template('orders/email/test.html')   
    html_content = txtmes.render(context_) 
    mail_subject = 'Tvoje objednavka'       
    to_email = request.user.email
    send_email = EmailMultiAlternatives(mail_subject, '', to=['luk.roztomily@seznam.cz'])
    send_email.mixed_subtype = 'related'
    send_email.attach_alternative(html_content, 'text/html')
    send_email.send()

    return JsonResponse(data)

def place_order(request, total = 0, quantity = 0):
    current_user = request.user

    cart_items = CartItem.objects.filter(user = current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    grand_total  = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.quantity * cart_item.product.price)
        quantity += cart_item.quantity
    
    tax = (total*2)/100
    grand_total = tax + total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt, dt)
            current_date = d.strftime("%Y%m%d")

            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            
            order = Order.objects.get(user =  current_user, is_ordered = False, order_number = order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total
                
            }
            return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')

def order_complete (request):
    order_number = request.GET.get('order_number')
    payment_id = request.GET.get('payment_id')
    try:    
        order = Order.objects.get(order_number= order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order_id = order.id)
        payment = Payment.objects.get(payment_id=payment_id)
        subtotal = 0

        for i in ordered_products:
            subtotal += i.quantity * i.product_price
        
        print(delivery_day(3, order.created_at))
        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'payment': payment,
            'subtotal': subtotal
            }


        return render(request, 'orders/order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')

def test (request):

        return render(request, 'orders/test.html')