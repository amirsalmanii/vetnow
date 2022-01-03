from django.urls import path
from . import views

app_name = 'threed'
urlpatterns = [
    path('threed/create/', views.ThreedCreate.as_view(), name="create_3d"),
    path('threed/<str:slug>/', views.ThreedViews.as_view(), name='show_3d_images'),
    path('threed/update/<str:slug>/', views.ThreedUpdate.as_view(), name='update_3d_images'),
    path('threed/delete/<str:slug>/', views.ThreedDelete.as_view(), name='delete_3d_images'),
]