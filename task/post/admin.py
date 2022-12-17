from django.contrib import admin

# Register your models here.
from .models import Post, Notification


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "state", "user")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "action", "user")




# def get_posts_for_user(request, username):
#     posts = Post.objects.filter(user__username=username)
#     return HttpResponse(posts)
# To define the URL for this view, you can add a new URL pattern to the urls.py file like this:

# Copy code
# from django.urls import path
# from .views import get_posts_for_user

# urlpatterns = [
#     path('posts/', get_posts, name='get_posts'),
#     path('posts/<str:username>/', get_posts_for_user, name='get_posts_for_user')
# ]
# Next, you will need to add a view for creating a user and inviting them to write. This view will need to take the username and email of the user as input parameters, and will create a new User object with these values. In Django, you can define this view like this:

# Copy code
# from django.http import HttpResponse
# from django.contrib.auth.models import User

# def create_user(request, username, email):
#     user = User.objects.create_user(username=username, email=email)
#     user.save()
#     return HttpResponse('User created')
# To define the URL for this view, you can add a new URL pattern to the urls.py file like this:

# Copy code
# from django.urls import path
# from .views import create_user

# urlpatterns = [
#     path('posts/', get_posts, name='get_posts'),
#     path('posts/<str:username>/', get_posts_for_user, name='get_posts_for_user'),
#     path('users/<str:username>/<str:email>/', create_user, name='create_user')
# ]
# With these additional views and URL patterns in place, a superuser will be able to get all posts for a particular user and create a user and invite them to write. You can add more features and functionality to the API as needed.



# To create an API that allows a superuser to see a list of notifications coming from users doing actions on posts, you will need to add a new model for the notifications and add some additional functionality to the API created in the previous answer.

# First, you will need to define a new Notification model that has fields for the user who performed the action and the type of action that was performed. In Django, you can define this model like this:

# Copy code
# from django.db import models
# from django.contrib.auth.models import User

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     action = models.CharField(max_length=255)
# Once you have defined the Notification model, you can use Django's built-in migrations to create the corresponding database table. To do this, you will need to run the following commands:

# Copy code
# python manage.py makemigrations
# python manage.py migrate
# Next, you will need to add some additional functionality to the views for creating and updating posts. When a user creates or updates a post, you will need to create a new Notification object to record the action. In Django, you can modify the create_post and update_post views like this:

# Copy code
# from django.http import HttpResponse
# from .models import Post, Notification

# def create_post(request, title, description, state, user_id):
#     post = Post.objects.create(title=title, description=description, state=state, user_id=user_id)
#     post.save()
#     notification = Notification.objects.create(user_id=user_id, action='created post')
#     notification.save()
#     return HttpResponse('Post created')

# def update_post(request, post_id, title, description, state, user_id):
#     post = Post.objects.get(id=post_id)
#     post.title = title
#     post.description = description
#     post.state = state
#     post.user_id = user_id
#     post.save()
#     notification = Notification.objects.create(user_id=user_id, action='updated post')
#     notification.save()
#     return HttpResponse('Post updated')
# With these changes in place, a new Notification object will be created whenever a user creates or updates a post.

# Finally, you will need to add a view for getting the list of notifications for the superuser. This view will need to return all Notification objects in the database. In Django, you can define this view like this:

# Copy code
# from django.http import HttpResponse
# from .models import Notification

# def get_notifications(request):
#     notifications = Notification.objects.all()
#     return HttpResponse(notifications)
# To define the URL for this view, you can add a new URL pattern to the urls.py file like this:

# Copy code
# from django.urls import path
# from .views import get_notifications

# urlpatterns = [
#     path('posts/', get_posts, name='get_posts'),
#     path('posts/<str:username>/', get_posts_for_user, name='get_posts_


