from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# class ClockEntry(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     longitude = models.CharField(max_length=100)
#     latitude = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.date
#
#     def get_absolute_url(self):
#         return reverse("clock_card:clock")
#
#     class Meta:
#         ordering = ('-date')
