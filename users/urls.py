from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('<int:id>/', views.main, name="main"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('schedule/<int:id>/', views.schedule, name="schedule"),
]

