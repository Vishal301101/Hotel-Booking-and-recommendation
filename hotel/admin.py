from django.contrib import admin
from .models import Hotel, Activity, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'ratings')
    search_fields = ('name', 'location')
 
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'activity_type', 'timestamp')
    list_filter = ('activity_type',)
    search_fields = ('user__username', 'hotel__name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'status_display')

    def status_display(self, obj):
        if obj.is_completed:
            return "Completed"
        elif obj.is_draft:
            return "Draft"
        else:
            return "Unknown Status"

    status_display.short_description = 'Status'