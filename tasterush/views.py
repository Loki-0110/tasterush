from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, HttpResponse
from django.db.models import Q

from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from django.conf import settings

from restaurant.forms import RestaurantRegForm
from restaurant.models import Dish, Restaurant
from user.forms import UserRegForm
from user.models import User


# Function to generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))


def my_view(request, form_type):
    if form_type == 'user_signup':
        form = UserRegForm(request.POST)
        type = 'user'
    elif form_type == 'add_restaurant':
        form = RestaurantRegForm(request.POST)
        type = 'restaurant'
    else:
        form = None
    if request.method == "POST":

        if form.is_valid():
            form.save()
        email = request.POST['email']

        # Generate and send OTP
        otp = generate_otp()
        subject = 'OTP for Verification'
        message = f'Your OTP is: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        # Store OTP in the session
        request.session['otp'] = otp

        return redirect('verify_otp')

    return render(request, 'register1.html')


def verify_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST['otp']
        stored_otp = request.session.get('otp')
        print(stored_otp)

        if user_entered_otp == stored_otp:
            # OTP is correct, redirect to success page
            return redirect('otp_success')
        else:
            return render(request, 'otp_verification.html', {'message': 'Invalid OTP. Please try again...'})

    return render(request, 'otp_verification.html')


def otp_success(request):
    return render(request, 'login1.html')


def register1(request, form_type):
    if form_type == 'user_signup':
        form = UserRegForm(request.POST)
    elif form_type == 'add_restaurant':
        form = RestaurantRegForm(request.POST)
    else:
        form = None
    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('my_view', {'form_type': form_type})
    # else:
    #     form = UserRegForm()
    return render(request, 'register1.html', {'form': form, 'form_type': form_type})


# views.py
from django.contrib import messages


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            print(user)
            request.session['user_id'] = user.id
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login1.html')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Remove the session variable
        messages.success(request, 'Logged out successfully')
    return redirect('home')


def search_results(request):
    query = request.GET.get('q', '')

    if query:
        # Filter the database for dishes that match the query
        dishes = Dish.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        dishes = []

    # Pass the query to the template for debugging
    return render(request, 'search_results.html', {'dishes': dishes, 'query': query})


import math


def home(request):
    popular_dishes = Dish.objects.all()[:4]
    return render(request, 'home.html', {'popular_dishes': popular_dishes})



def about(request):
    return render(request, 'about.html')
