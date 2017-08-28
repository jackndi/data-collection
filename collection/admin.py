# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Brand, Location, Person, Data


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        fields = ('name', 'company', 'updated', 'description')


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
    list_display = ('name', 'company', 'description', 'updated')
    list_filter = ('updated', 'company')
    search_fields = ['name', 'description', 'company']
    ordering = ['name', 'updated']


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'updated', 'description')


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource
    list_display = ('name', 'latitude', 'longitude', 'updated', 'description')
    list_filter = ('updated',)
    search_fields = ['name', 'description', 'latitude', 'longitude']
    ordering = ['name', 'latitude', 'longitude', 'updated']


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'gender', 'age', 'updated', 'description')


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    list_display = ('first_name', 'last_name', 'gender', 'age', 'description')
    list_filter = ('gender', 'age', 'updated')
    search_fields = ['first_name', 'last_name', 'description']
    ordering = ['first_name', 'last_name', 'age', 'gender']


class DataResource(resources.ModelResource):
    class Meta:
        model = Data
        fields = ('collector__username', 'brand__name', 'location__name',
                  'person__first_name', 'updated', 'description')


@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    resource_class = DataResource
    list_display = ('collector', 'brand', 'location', 'person', 'description')
    list_filter = ('collector__username', 'updated')
    search_fields = ['location', 'brand', 'description']
    ordering = ['brand', 'updated', 'collector']
