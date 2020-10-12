from django.urls import path
from . import views

app_name ="picks"
urlpatterns = [
    path('lohbs_pick/', views.lohbs_pick, name="lohbs_pick"),
]