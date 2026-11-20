from django.db.models.aggregates import Sum

from openai_api.client import get_car_ai_bio

# I import the 4 signals django: notifications he sends out automatic before and after save or empty a obj.
from django.db.models.signals import post_save, post_delete, pre_save

# I import o receiver, the decorater what call a function the a signal.
from django.dispatch import receiver

# I import the model Car, what is who to go sends signals
from cars.models import Car
from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum("value"))["total_value"]
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.bio = ai_bio


# I 'll call is function the signal post_save, what sends after the a car is save.
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


# I'll call is function the signal post_delete, what sends after the a car is empty
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
