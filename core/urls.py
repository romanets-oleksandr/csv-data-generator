from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('authentication.urls')),
    path('', include('csv_generator.urls')),
    path('admin/', admin.site.urls),
]
