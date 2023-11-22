from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('hotel_detail/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/<int:hotel_id>/draft_booking/', views.draft_booking, name='draft_booking'),
    path('hotel/<int:hotel_id>/completed_booking/', views.completed_booking, name='completed_booking'),
    path('recommendations/<int:user_id>/', views.get_recommendations, name='recommendations'),
    path('Home/', views.Home, name='Home'),
    path('register_login/', views.register_login, name='register_login'),
    path('hotel_detail/<int:hotel_id>/', views.visit_hotel, name='visit_hotel'),
    path('', views.Home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
