from django.urls import path
from . import views

app_name ="products"
urlpatterns = [
    path('products_list/', views.products_list, name="products_list"),
]