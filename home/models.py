from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Reserved"))

# This is the Cottage model
class Cottage(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    sq_ft = models.IntegerField()
    clean_date = models.ForeignKey('Reservation', on_delete=models.SET_NULL, null=True, blank=True, related_name='clean_cottages')
    water_filter = models.IntegerField(blank=True)
    water_filter_replace = models.DateField(blank=True)
    fireplace = models.IntegerField(blank=True)

    # This selects the cottage to go with the date for cleaning
    def __str__(self):
        return f"Cottage {self.id}"

# This is the reservation model
class Reservation(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    # This displays the cottage id and the date range of the reservation
    def __str__(self):
        return f"{self.cottage.id}: {self.start} → {self.end}"
