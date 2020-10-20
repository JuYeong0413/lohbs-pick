from django.urls import path
from . import views

app_name ="products"
urlpatterns = [
    path('', views.main, name="main"),
    path('search/', views.search, name="search"),
    path('category_list/', views.category_list, name="category_list"),
    # path('collection_add/<int:product_id>/<int:collection_id>/', views.collection_add, name="collection_add"),
]