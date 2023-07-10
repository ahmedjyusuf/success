from django.urls import path
# from .views import get_current_user
from . import views
urlpatterns = [
    path('local-class/', views.localized_zoom_time, name='local_class'),
]
