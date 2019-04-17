from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#Create your models here.
class ClockEntry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    street = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    work_st = models.CharField(max_length=100)
    clock_io = models.CharField(max_length=100)
    hours_worked = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("clock_card:clock_entry")

    class Meta:
        ordering = ('-date', )
