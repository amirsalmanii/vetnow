from django.urls import path
from . import views

urlpatterns = [
    path('gains/<str:slug>/', views.ComputeGain.as_view(), name='categories_gains'),
]