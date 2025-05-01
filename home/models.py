from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Cottage(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=2)
    sq_ft = models.IntegerField()
    clean = models.DateField(ForeignKey=True, on_delete=models.CASCADE)
    water_filter = models.IntegerField()
    water_filter_replace = models.DateField()
    fireplace = models.IntegerField()
