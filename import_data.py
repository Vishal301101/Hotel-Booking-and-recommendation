import json
from hotel.models import Hotel

with open('/home/vishal/Desktop/hotel/hotel/data/hotels.json') as json_file:
    hotels_data = json.load(json_file)

for hotel_data in hotels_data:
    Hotel.objects.create(
        name=hotel_data['name'],
        location=hotel_data['location'],
        price=hotel_data['price'],
        amenities=hotel_data['amenities'],
        ratings=hotel_data['ratings']
    )
    print(f"Created hotel: {hotel_data['name']}")
