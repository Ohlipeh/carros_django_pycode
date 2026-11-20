# I import the 4 signals django: notifications he sends out automatic before and after save or empty a obj.
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
# I import o receiver, the decorater what call a function the a signal.
from django.dispatch import receiver
# I import the model Car, what is who to go sends signals
from cars.models import Car

# I'll call this function the signal pre_save: sender=Car make it run only for cars and not for others models
@receiver(pre_save, sender=Car)
# I create the function what run before the a car is save. Instance is the car what is being save, and the **kwargs receive informations exes django.
def car_pre_save(sender, instance, **kwargs):
    # I show a mensage in terminal, for I see the moment in what signal sends.
    print("### PRE SAVE ###")

# I 'll call is function the signal post_save, what sends after the a car is save.
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    # I show a mensage in terminal
    print("### POST SAVE ###")

# I'll call is function the signal pre_delete, what sends before the a car is empty
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    # I show a mensage in terminal
    print("### PRE DELETE ###")

# I'll call is function the signal post_delete, what sends after the a car is empty
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    # I show a mensage in terminal
    print("### POST DELETE ###")