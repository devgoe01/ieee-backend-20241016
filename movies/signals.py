from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Wallet

@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()