from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category


@receiver(post_save, sender=User)
def create_default_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(name='Home', user=instance)
        Category.objects.create(name='Work', user=instance)