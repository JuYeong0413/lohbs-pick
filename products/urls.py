from django.urls import path
from . import views

app_name ="products"
urlpatterns = [
    path('', views.main, name="main"),
    path('search/', views.search, name="search"),
    path('category_list/', views.category_list, name="category_list"),
]