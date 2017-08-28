# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Brand, Person, Location, Data


class DataTestCase(TestCase):
    def create_brand(self):
        return Brand(name='Sprite', company='Coca Cola', description='Green bottle')

    def create_location(self):
        return Location(name='Mathare', latitude='34.393939', longitude='54.838383', description='highly propulated')

    def create_person(self):
        return Person(first_name='John', last_name='Doe', age=30, gender='male', description="tall man")

    def test_brand_creation(self):
        brand = self.create_brand()
        self.assertTrue(isinstance(brand, Brand))
        self.assertTrue(brand.__unicode__(), "{}".format(brand.name))

    def test_location_creation(self):
        location = self.create_location()
        self.assertTrue(isinstance(location, Location))
        self.assertTrue(location.__unicode__(), "{}".format(location.name))

    def test_person_creation(self):
        person = self.create_person()
        self.assertTrue(isinstance(person, Person))
        self.assertTrue(person.__unicode__(), "{} {}".format(person.first_name, person.last_name))

    # todo add the request and response test case