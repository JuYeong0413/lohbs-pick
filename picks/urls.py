from django.urls import path
from . import views

app_name ="picks"
urlpatterns = [
    path('lohbs_pick/', views.lohbs_pick, name="lohbs_pick"),
    path('delete/<int:collection_id>/', views.delete, name="delete"),
    path('delete_cp/<int:cp_id>/<int:collection_id>/', views.delete_cp, name="delete_cp"),
    path('collection_add/', views.collection_add, name="collection_add"),
    path('create_cp/<int:product_id>/', views.create_cp, name="create_cp"),
    path('collection_update/<int:collection_id>/', views.collection_update, name="collection_update"),

    ## 공유 관련
    path('shared/', views.shared, name="shared"),
    path('<int:collection_id>/share/', views.share_new, name="share_new"),
    path('create/', views.share_create, name="share_create"),
    path('<int:id>/edit/', views.share_edit, name="share_edit"),
    path('<int:id>/update/', views.share_update, name="share_update"),
    path('<int:id>/delete/', views.share_delete, name="share_delete"),
]