"""
    Household Member Model
"""
from django.db import models
from .profile import Profile


class Member(models.Model):
    """
    Stores the properties of a household member
    Related data: Profile (extended user)
    Properties:
        height - in inches
        weight - in pounds
    """
    name = models.CharField(max_length=75)
    gender = models.CharField(max_length=10)
    height = models.IntegerField()
    weight = models.IntegerField()
    dob = models.DateField()

    # Related data
    profile = models.ForeignKey(
        Profile, on_delete=models.DO_NOTHING, related_name='member')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("member")
        verbose_name_plural = ("members")
