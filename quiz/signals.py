from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Baza, Category

def update_category_count(category):
    category.count = Baza.objects.filter(category=category).count()
    category.save()

@receiver(post_save, sender=Baza)
def update_count_on_save(sender, instance, **kwargs):
    update_category_count(instance.category)

@receiver(post_delete, sender=Baza)
def update_count_on_delete(sender, instance, **kwargs):
    update_category_count(instance.category)
