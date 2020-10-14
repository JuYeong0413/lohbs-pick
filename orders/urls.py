from django.urls import path
from .views import *

app_name ="orders"
urlpatterns = [
    path('', main, name="main"),
    path('<int:id>/', show, name="main"),
    path('new/', new, name="main"),
]