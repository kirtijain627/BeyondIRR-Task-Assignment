from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Post, Notification

@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):  
    if created:
        print("signal fired post created")
        Notification.objects.create(
                post=Post.objects.get(id=instance.id),
                action="created",
                user=instance.user
            )
       
    else:
        print("signal fired post updated")    
        
        Notification.objects.create(
                post=Post.objects.get(id=instance.id),
                action="updated",
                user=instance.user
            )
        
    
    
@receiver(pre_delete, sender=Post)
def send_notification_delete(sender, instance, **kwargs):
    print("signal fired post deleted")
    Notification.objects.create(
                post=Post.objects.get(id=instance.id),
                action="deleted",
                user=instance.user
            )
   