# Import the path function for defining URL patterns
from django.urls import path
# Import views from the current package
from . import views

# Define URL patterns for this app
urlpatterns = [
    # Map the root URL to the index view, name it 'home'
    path('', views.index, name='home'),
]