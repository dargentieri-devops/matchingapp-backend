from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('matchinapp.urls')),
    path('admin/', admin.site.urls),
]
