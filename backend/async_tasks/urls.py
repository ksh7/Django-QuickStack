from django.urls import path
from . import views

app_name = "async_tasks"

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('website_carbon_footprint', views.website_carbon_footprint, name='website_carbon_footprint'),
    path('get_coffee_picture', views.get_coffee_picture, name='get_coffee_picture'),
    path('get_latest_coffee_picture', views.get_latest_coffee_picture, name='get_latest_coffee_picture'),
]
