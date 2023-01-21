from django.contrib import admin
from django.urls import path, include
from post import views

urlpatterns = [
    path("",views.login),
    path('admin/', admin.site.urls),
    path('api/', include('post.urls')),
]
