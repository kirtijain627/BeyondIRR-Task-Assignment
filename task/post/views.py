# from .serializers import UserSerializer
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post, Notification
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect('/api/post/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


# using rest framework
@csrf_exempt
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def post(request, post_id=None):
    if request.method == "GET":
        if request.user.is_superuser:
            posts = Post.objects.filter(~Q(state='archived'))
        else:
            id = post_id
            if id is not None:
                posts = Post.objects.filter(id=id, user= request.user)
            else:  
                posts = Post.objects.filter(user=request.user)
            
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        user = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            
        # Send a notification to the admin that the post was created
            # notification = Notification.objects.create(
            #     post=Post.objects.get(id=serializer.data['id']),
            #     action="created",
            #     user=user
            # )
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == "PUT":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        
        print(post.description)
        print(user)

        if post.user == user:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
        # # Send a notification to the admin that the post was updated
        #         notification = Notification.objects.create(
        #             post=post,
        #             action="updated",
        #             user=user
        #         )

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    elif request.method == "PATCH":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        print(post.description)
        print(user)

        if post.user == user:
            serializer=PostSerializer(post, data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
               
        # Send a notification to the admin that the post was updated
                # notification = Notification.objects.create(
                #     post=post,
                #     action="updated",
                #     user=user
                # )
        
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    elif request.method == "DELETE":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        
        if post.user == user:
            # notification = Notification.objects.create(
            #     post=post,
            #     action="deleted",
            #     user=user
            # )
            post.delete()
            
            return Response({'msg':'Data Deleted'})
    
    
@api_view(["GET"])                 #for getting posts of a particular user
def get_posts_for_user(request, username):
    print(username)
    if request.user.is_superuser:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(~Q(state='archived'), user=user)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    
    
def list_notifications(request):
    if request.user.is_superuser:
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        
        
        return  render(request, 'notifications.html', {'notifications': serializer.data})
    
        # return JsonResponse('notifications.html', {'notifications': serializer.data}, safe= False)  # for json response     
    else:
        return HttpResponse("You are not authorized to view this page")