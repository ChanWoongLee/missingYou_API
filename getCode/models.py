#models.py

from django.db import models


class Animal(models.Model):
    animal_name = models.CharField(max_length=15, primary_key=True)
    animal_code = models.CharField(max_length=10)


