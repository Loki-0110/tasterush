from django.contrib import messages
from django.shortcuts import render, redirect
import math
from .models import Restaurant, Dish




def restaurant_dishes(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    dishes = Dish.objects.filter(restaurant=restaurant)

    return render(request, 'dishes.html', {'restaurant': restaurant, 'dishes': dishes})


def disp_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes.html', {'dishes': dishes})

def calculate_total_cost(selected_dish_ids):
    # Fetch the selected dishes from the database
    selected_dishes = Dish.objects.filter(id__in=selected_dish_ids)

    # Calculate total cost (sum of dish prices)
    total_cost = sum(dish.price for dish in selected_dishes)

    return total_cost



def nearby_restaurants(request, user_latitude, user_longitude):
    # Convert user_latitude and user_longitude to floats
    user_latitude = float(user_latitude)
    user_longitude = float(user_longitude)

    # Calculate the radius (in kilometers) for searching nearby restaurants
    # Adjust this value as needed for your application
    search_radius = 10000.0

    # Calculate nearby restaurants using the Haversine formula or a similar method
    nearby_restaurants = []

    for restaurant in Restaurant.objects.all():
        restaurant_latitude = float(restaurant.latitude)
        restaurant_longitude = float(restaurant.longitude)
        print(restaurant.name)
        print(restaurant_latitude)
        print(restaurant_longitude)
        # Haversine formula to calculate the distance between two points on Earth
        radius = 6371  # Earth radius in kilometers
        lat1 = math.radians(user_latitude)
        lon1 = math.radians(user_longitude)
        lat2 = math.radians(restaurant_latitude)
        lon2 = math.radians(restaurant_longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c

        if distance <= search_radius:
            nearby_restaurants.append({'restaurant': restaurant, 'distance': round(distance)})
        print(nearby_restaurants)
    return render(request, 'nearby_restaurants.html', {'nearby_restaurants': nearby_restaurants})

def restaurant_home(request):
    return render(request, 'restaurant_home.html')