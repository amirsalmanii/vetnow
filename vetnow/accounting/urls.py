from django.urls import path
from . import views

urlpatterns = [
    path('gains/<slug:slug>/', views.ComputeGain.as_view(), name='categories_gains'),
]