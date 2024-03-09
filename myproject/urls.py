# myproject/urls.py
from django.contrib import admin
from django.urls import include, path
from myapp.views import show_all  # Import the show_all view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_all, name='show_all_default'),  # Redirect to the show_all view
    path('myapp/', include('myapp.urls')),  # Include the URLs from myapp
]
