"""
    Food Model
"""
from django.db import models
from .profile import Profile


class Food(models.Model):
    """
    Stores the properties of a food item
    Related data: Profile (extended user)
    """
    name = models.CharField(max_length=75)
    brand = models.CharField(max_length=75)
    quantity = models.IntegerField()
    ounces = models.DecimalField(max_digits=10, decimal_places=2)
    servings = models.IntegerField()
    calories_per_serving = models.IntegerField()
    container = models.CharField(max_length=25)
    expiration_date = models.DateField()

    # Related data
    profile = models.ForeignKey(
        Profile, on_delete=models.DO_NOTHING, related_name='food')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("food")
        verbose_name_plural = ("foods")
