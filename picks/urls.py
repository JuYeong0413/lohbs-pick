from django.urls import path
from . import views

app_name ="picks"
urlpatterns = [
    path('lohbs_pick/', views.lohbs_pick, name="lohbs_pick"),
    ## 공유 관련
    path('shared/', views.shared, name="shared"),
    path('share/', views.share_new, name="share_new"),
    path('create/', views.share_create, name="share_create"),
    path('<int:id>/edit/', views.share_edit, name="share_edit"),
    path('<int:id>/update/', views.share_update, name="share_update"),
    path('<int:id>/delete/', views.share_delete, name="share_delete"),
]