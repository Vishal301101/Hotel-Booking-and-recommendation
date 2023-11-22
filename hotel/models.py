# hotel/models.py
from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amenities = models.TextField()
    ratings = models.FloatField()
 
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=[
        ('visit', 'Visit'),
        ('draft_booking', 'Draft Booking'),
        ('completed_booking', 'Completed Booking')
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.hotel.name}"
    
    def get_score(self):
        # Define your logic to calculate the score based on the activity type
        # Example: Assign different scores for different activities
        if self.activity_type == 'visit':
            return 1
        elif self.activity_type == 'booking':
            return 2
        else:
            return 0

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name} - {'Completed' if self.is_completed else 'Draft'}"

    def save(self, *args, **kwargs):
        
        if self.is_completed:
            
            print(f"Booking for {self.hotel.name} marked as completed.")
        elif self.is_draft:
            
            print(f"Booking for {self.hotel.name} saved as a draft.")
        
        super().save(*args, **kwargs)