from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Brand, Person, Location, Data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('url', 'id', 'name', 'company', 'description')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'description')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'id', 'name', 'latitude', 'longitude', 'description')


class DataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Data
        fields = ('url', 'id', 'collector', 'person', 'brand', 'location', 'description')
