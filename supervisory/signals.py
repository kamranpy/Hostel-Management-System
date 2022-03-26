from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)  # Assigning new users to customer group
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)  # Creating a customer with user


post_save.connect(customer_profile, sender=User)

