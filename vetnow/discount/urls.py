from django.urls import path
from . import views

urlpatterns = [
    path('discunt_add/', views.DiscuntCreate.as_view(), name='discunt_create'),
]