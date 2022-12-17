from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Post, Notification


@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):  
    if created:
        print("signal fired post created")
    else:
        print("signal fired post updated")     
    
    
@receiver(pre_delete, sender=Post)
def send_notification_delete(sender, instance, **kwargs):
    print("signal fired post deleted")
 
   