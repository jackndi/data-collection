# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    """
    Information of the Brand to be collected
    """
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-updated',)


class Person(models.Model):
    """
    Details of the person data is being collected from
    """
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
        ('Not Disclose', 'not_disclose'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('-updated',)


class Location(models.Model):
    """
    Details of the data collection location
    """
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-updated',)


class Data(models.Model):
    """
    All collected pieces of information together
    """
    collector = models.ForeignKey(User, related_name="collections")
    person = models.ForeignKey(Person, related_name="my_data")
    brand = models.ForeignKey(Brand, related_name="data")
    location = models.ForeignKey(Location, related_name="location_data")
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{} : {} : {}".format(self.brand, self.collector, self.location)

    class Meta:
        ordering = ('-updated',)