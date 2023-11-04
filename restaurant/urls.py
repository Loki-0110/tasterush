from django.urls import path
from . import views

urlpatterns = [
    path('nearby_restaurants/<str:user_latitude>/<str:user_longitude>/', views.nearby_restaurants, name='nearby_restaurants'),
    path('restaurant_dishes/<int:restaurant_id>/', views.restaurant_dishes, name='restaurant_dishes'),
    path('disp_dishes/', views.disp_dishes, name='disp_dishes'),
    path('restaurant', views.restaurant_home, name='restaurant_home'),


]

