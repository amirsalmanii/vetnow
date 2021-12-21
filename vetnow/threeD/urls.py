from django.urls import path
from . import views

app_name = 'threed'
urlpatterns = [
    path('threed/<slug:slug>/', views.ThreedViews.as_view(), name='show_3d_images'),
    path('threed/update/<slug:slug>/', views.ThreedUpdate.as_view(), name='update_3d_images'),
]