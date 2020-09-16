"""
    Water Model
"""
from django.db import models
from .profile import Profile


class Water(models.Model):
    """
    Stores the properties of a water item
    Related data: Profile (extended user)
    """
    name = models.CharField(max_length=75)
    quantity = models.IntegerField()
    ounces = models.DecimalField(max_digits=10, decimal_places=2)
    container = models.CharField(max_length=25)

    # Related data
    profile = models.ForeignKey(
        Profile, on_delete=models.DO_NOTHING, related_name='water')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("water")
        verbose_name_plural = ("waters")
