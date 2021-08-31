from .models import profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save,sender=User)
def post_save_creat_profile(sender,instance,created,*args, **kwargs):
    if created:
        profile.objects.create(user=instance)
