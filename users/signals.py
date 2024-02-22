from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User #(sender)
from django.dispatch import receiver # connects a signal with a function, so that the function gets called every time the signal is sent




# when a user is saved, send a signal tp createProfile to create a profile
@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if user created, create a profile ohbject with an instance of user
    if created:
        Profile.objects.create(user=instance)
        
        
        
        
@receiver (post_save, sender=User)
def save_profile(sender, instance,**kwargs):
    # if user created, create a profile ohbject with an instance of user
    instance.profile.save()