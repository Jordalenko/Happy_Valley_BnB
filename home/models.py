from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    # clean_date = models.ForeignKey(
    #     'Reservation', on_delete=models.SET_NULL, null=True, blank=True,
    #     related_name='clean_date'
    # )
    water_filter = models.IntegerField(null=True, blank=True)
    water_filter_replace = models.DateField(null=True, blank=True)
    fireplace = models.IntegerField(null=True, blank=True)

    # This selects the cottage to go with the date for cleaning
    def __str__(self):
        return f"Cottage {self.cottage_id}"
    

# This is the guest model 
class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    email = models.TextField()
    bank = models.IntegerField(null=True, blank=True)
    credit_card = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f"Guest {self.name}: {self.guest_id}"


# This is the reservation model
class Reservation(models.Model):
    res_id = models.CharField(
        primary_key=True,
        unique=True,
        max_length=20,
        editable=False
    )
    cottage = models.ForeignKey(
        Cottage,
        on_delete=models.CASCADE,
        related_name="reserved"
    )
    start = models.DateField()
    end = models.DateField()
    guest_id = models.ForeignKey(
        'Guest', on_delete=models.CASCADE, related_name="reservations", null=True, 
        blank=True
    )
    discount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Cottage {self.cottage.cottage_id}: {self.start} → {self.end} by {self.guest_id} # {self.res_id}"

    def save(self, *args, **kwargs):
        creating = not self.pk  # Check if this is a new instance (optional)

    # Generate a unique reservation ID if not set
        if not self.res_id:
            year = now().year
            last = Reservation.objects.filter(res_id__startswith=str(year)).order_by('-res_id').first()
            if last:
                last_number = int(last.res_id[-4:])
                new_number = last_number + 1
            else:
                new_number = 1
            self.res_id = f"{year}{new_number:04d}"

        # Save the reservation
        super().save(*args, **kwargs)

        # If reservation is marked complete, move it to the Complete model if not already there
        if getattr(self, "is_complete", False) and not Complete.objects.filter(res_id=self).exists():
            Complete.objects.create(
                cottage=self.cottage,
                start=self.start,
                end=self.end,
                guest_id=self.guest_id,
                discount=self.discount,
                res_id=self
            )
    class Meta:
        ordering = ["-created_on"]
    

# This is the completed bookings model
class Complete(models.Model):
    cottage = models.ForeignKey(
        Cottage, on_delete=models.CASCADE,
        related_name="cottage_completed"
    )
    start = models.DateField()
    end = models.DateField()
    guest_id = models.ForeignKey(
        'Guest', on_delete=models.CASCADE,
        related_name="completed_reservations", null=True, blank=True
    )
    discount = models.IntegerField(default=0)
    res_id = models.ForeignKey(
        'Reservation', on_delete=models.CASCADE, related_name="reserver", null=True, 
        blank=True
    )
