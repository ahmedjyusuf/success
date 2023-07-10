from django.urls import path
# from .views import get_current_user
from . import views
urlpatterns = [
    path('api/', views.get_current_user, name='current_user'),
    path('names/', views.names, name='namesx'),
    # Add other URL patterns for your application
]
