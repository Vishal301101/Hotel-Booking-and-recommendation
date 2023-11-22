from django.core.management.base import BaseCommand
from hotel.models import Hotel
import json

class Command(BaseCommand):
    help = 'Imports hotel data from a JSON file'

    def handle(self, *args, **options):
        with open('/home/vishal/Desktop/hotel/hotel/data/hotels.json') as json_file:
            hotels_data = json.load(json_file)

        for hotel_data in hotels_data:
            Hotel.objects.create(
                id=hotel_data['id'],
                name=hotel_data['name'],
                location=hotel_data['location'],
                price=hotel_data['price'],
                amenities=hotel_data['amenities'],
                ratings=hotel_data['ratings']
            )
            self.stdout.write(self.style.SUCCESS(f"Created hotel: {hotel_data['name']}"))

