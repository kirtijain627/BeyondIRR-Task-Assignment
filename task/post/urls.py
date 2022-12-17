from . import views
from django.urls import path

urlpatterns = [
   
    path('post/', views.post),
    path('post/<int:post_id>/', views.post),
    path('posts/<str:username>/', views.get_posts_for_user, name='get_posts_for_user'),
    path('notification/', views.list_notifications),
    
]
