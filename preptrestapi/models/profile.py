"""
    Profile Model
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to extend the user model with additional properties
    adds:
    Properties:
        water goal (int) - the number of days' worth of water to prep
        food goal (int) - the number of days' worth of food to prep
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    water_goal = models.IntegerField()
    food_goal = models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")
