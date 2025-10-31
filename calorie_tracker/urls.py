from django.urls import path
from . import views

app_name = 'calorie_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('reset/', views.reset_items, name='reset_items'),
]
