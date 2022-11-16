from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    set_category = (
            "Забота о себе" , 
            "Зарплата" , 
            "Здоровье и фитнес" , 
            "Кафе и рестораны" , 
            "Машина" , "Образование" , 
            "Отдых и развлечения" , 
            "Платежи, комиссии" , 
            "Покупки: одежда, техника" , 
            "Продукты" , 
            "Проезд"
            )
    if created:
        for i in set_category:
           c = Category.objects.create(name = i, user  = instance)
           c.save()