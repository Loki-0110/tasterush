from django.urls import path, include
from . import views

urlpatterns = [
    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('order/', views.order_now, name='order_now'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    # path('track_order/<int:order_id>/', views.track_order, name='track_order'),
]