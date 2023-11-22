from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from .models import Hotel, Activity, Booking
from .forms import CustomUserCreationForm
from django.db import models
from django.db.models import Case, When, Sum, F

import json

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    user = request.user
    Activity.objects.create(user=user, hotel=hotel, activity_type='visit')
    
    recommended_hotels = get_recommendations(user.id)[:4]

    print(f"User visited Hotel ID {hotel_id}")
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'recommended_hotels': recommended_hotels})

def register_login(request):
    register_form = CustomUserCreationForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        action = request.POST.get('action', None)

        if action == 'register':
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                auth_login(request, user)
                return redirect('Home')
        elif action == 'login':
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('Home')

    return render(request, 'register_login.html', {'register_form': register_form, 'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('register_login')


def draft_booking(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    user = request.user

    booking = Booking.objects.create(user=user, hotel=hotel, is_draft=True)

    print(f"User made a draft booking for Hotel ID {hotel_id}, Booking ID: {booking.id}")
    return render(request, 'draft_booking.html', {'hotel': hotel, 'user': user, 'booking': booking})

def completed_booking(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    user = request.user

    booking = Booking.objects.create(user=user, hotel=hotel, is_completed=True)

    print(f"User completed a booking for Hotel ID {hotel_id}, Booking ID: {booking.id}")
    return render(request, 'completed_booking.html', {'hotel': hotel, 'user': user, 'booking': booking})

def Home(request):
    with open('/home/vishal/Desktop/hotel/hotel/data/hotels.json') as json_file:
        hotels = json.load(json_file)

    return render(request, 'home.html', {'hotels': hotels})

def get_recommendations(user_id):
    visited_hotel_ids = Activity.objects.filter(user_id=user_id, activity_type='visit').values_list('hotel_id', flat=True)
    
    recommended_hotels = Hotel.objects.exclude(id__in=visited_hotel_ids).annotate(
        total_score=Sum(Case(When(activity__user_id=user_id, activity__activity_type='visit', then=1), default=0, output_field=models.IntegerField()))
        + F('ratings')
    ).order_by('-total_score')[:3]

    return recommended_hotels

@login_required(login_url='/register_login/')
def visit_hotel(request, hotel_id):

    if request.user.is_authenticated:
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        Activity.objects.create(user=request.user, hotel=hotel, activity_type='visit')
        return redirect('hotel_detail', hotel_id=hotel_id)
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect('register_login')