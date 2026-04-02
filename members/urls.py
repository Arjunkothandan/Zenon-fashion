from django.urls import path
from . import views


urlpatterns = [
    path('members/',views.landing,name= 'landing'),
    path('members/home/',views.main,name = 'main'),
    path('members/aboutus/',views.aboutus,name='aboutus'),
    path('members/contactus/',views.contactus, name = 'contactus'),
    path('category/<int:id>/', views.category_detail,name='category_detail'),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:cart_id>/', views.remove_item, name='remove_item'),
    path('search/', views.search, name='search'),
    path("cart/", views.cart, name="cart"),
    path("payment/", views.payment, name="payment"),
    path("place-order/", views.place_order, name="place_order"),
    path('checkout/', views.checkout, name='checkout'),
    path("order-success/", views.order_success, name="order_success"),

]