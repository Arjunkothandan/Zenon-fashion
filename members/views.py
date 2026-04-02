from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from . models import *
from . models import Catagory,Cart
from .models import Product
from django.db.models import Q
from .models import CartItem, Order
import razorpay
from django.conf import settings
from django.shortcuts import render


def main(request):
    catagory = Catagory.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, "main.html", {
        "catagory": catagory,
        "cart_count": cart_count
    })

def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def contactus(request):
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())

def category_detail(request, id):
    item = get_object_or_404(Catagory, id=id)
    return render(request, 'category_detail.html',{'item': item})

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())
    
def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')





def cart(request):

    items = Cart.objects.filter(user=request.user)

    cart_count = items.count()

    return render(request, "cart.html", {
        "items": items,
        "cart_count": cart_count
    })




def increase_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.quantity += 1
    item.save()
    return redirect('cart')


def decrease_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


def remove_item(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    return redirect('cart')


def search(request):

    query = request.GET.get('q')

    results = []

    if query:
        results = Catagory.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'results': results,
        'query': query
    }

    return render(request,'search_results.html',context)



def order_success(request):

    cart_items = Cart.objects.filter(user=request.user)

    orders = []
    total = 0

    # If cart has items (Add to Cart flow)
    if cart_items.exists():

        for item in cart_items:

            order = Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity
            )

            orders.append(order)
            total += order.total_price

        cart_items.delete()

    # If cart is empty (Buy Now flow)
    else:

        product_id = request.GET.get("product_id")

        if product_id:

            product = Product.objects.get(id=product_id)

            order = Order.objects.create(
                user=request.user,
                product=product,
                quantity=1,
                total_price=product.price
            )

            orders.append(order)
            total = product.price

    return render(request, "order_success.html", {
        "orders": orders,
        "total": total
    })








def place_order(request):
    if request.method == "POST":

        items = Cart.objects.filter(user=request.user)

        for item in items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity
            )

        items.delete()

        return redirect("order_success")


def checkout(request):
    cart_items = Cart.objects.all()

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, "payment.html", {
        "cart_items": cart_items,
        "total": total
    })


def payment(request):
    items = Cart.objects.filter(user=request.user)

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    amount = int(total * 100)  # Razorpay uses paise

    return render(request, "payment.html", {
        "items": items,
        "total": total,
        "amount": amount,
        "RAZORPAY_KEY_ID": settings.RAZORPAY_KEY_ID
    })




# Create your views here.
