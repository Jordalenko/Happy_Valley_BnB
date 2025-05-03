from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Reserved"))


# This is the Cottage model
class Cottage(models.Model):
    cottage_id = models.CharField(
        primary_key=True,
        max_length=1,
        null=False,
        default="A"
    )
    sq_ft = models.IntegerField()
    clean_date = models.ForeignKey(
        'Reservation', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='clean_date'
    )
    water_filter = models.IntegerField(null=True, blank=True)
    water_filter_replace = models.DateField(null=True, blank=True)
    fireplace = models.IntegerField(null=True, blank=True)

    # This selects the cottage to go with the date for cleaning
    def __str__(self):
        return f"Cottage {self.cottage_id}"
    

# This is the reservation model
class Reservation(models.Model):
    cottage = models.ForeignKey(
        Cottage,
        on_delete=models.CASCADE,
        related_name="reserved"
    )
    start = models.DateField()
    end = models.DateField()
    guest_id = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="reserver", null=True, 
        blank=True
    )
    discount = models.ForeignKey(
        Guest,
        on_delete=models.CASCADE,
        related_name="reservation_discounts",
        default=5
        )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cottage.id}: {self.start} → {self.end}"
    

# This is the completed bookings model
class Complete(models.Model):
    cottage = models.ForeignKey(
        Cottage, on_delete=models.CASCADE,
        related_name="cottage_completed"
        )
    start = models.DateField()
    end = models.DateField()
    guest_id = models.ForeignKey(
        Guest, on_delete=models.CASCADE,
        related_name="user_completed", null=True, blank=True
        )
    discount = models.ForeignKey(
        Guest, on_delete=models.CASCADE,
        related_name="complete_discount", default=5
        )


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    email = models.TextField()
    bank = models.IntegerField()
    credit_card = models.IntegerField()
    discount = models.IntegerField(default=0)


# This is the string representation of the completed bookings
class Meta:
    ordering = ["-created_on"]