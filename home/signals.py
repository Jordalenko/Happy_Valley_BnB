# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import Reservation, Cottage

# def update_clean_date(cottage):
#     latest = Reservation.objects.filter(cottage=cottage) \
#         .order_by('-end').first()
#     cottage.clean = latest.end if latest else None
#     cottage.save(update_fields=['clean'])

# @receiver(post_save, sender=Reservation)
# def update_clean_on_save(sender, instance, **kwargs):
#     update_clean_date(instance.cottage)

# @receiver(post_delete, sender=Reservation)
# def update_clean_on_delete(sender, instance, **kwargs):
#     update_clean_date(instance.cottage)