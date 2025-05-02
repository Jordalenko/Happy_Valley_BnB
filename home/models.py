from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Cottage(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    sq_ft = models.IntegerField()
    clean_date = models.ForeignKey('Reservation', on_delete=models.SET_NULL, null=True, blank=True, related_name='clean_cottages')
    water_filter = models.IntegerField(default=False)
    water_filter_replace = models.DateField()
    fireplace = models.IntegerField(default=False)

    def __str__(self):
        return f"Cottage {self.id}"


class Reservation(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.cottage.id}: {self.start} → {self.end}"