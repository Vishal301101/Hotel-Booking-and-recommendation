from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .hotel import views
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_login/', views.register_login, name='register_login'),
    path('Home/', views.Home, name='Home'),
    path('', include('hotel.urls')),  
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
