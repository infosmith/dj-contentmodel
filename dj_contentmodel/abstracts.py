# -*- coding: utf-8 -*-
"""
Abstract classes for creating taxonomies. Inherit from these classes as needed.
    -See models.py for examples.
    -Delete classes in models.py to remove included sitemap.
"""
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from taggit.managers import TaggableManager


class Group(MPTTModel):
    """Tree is queried by group but authentication and authorization has not been implemented"""
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Taxonomy(MPTTModel):
    """Inherit from Taxonomy to create taxons."""
    groups = TreeManyToManyField('Group')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    collections = models.ManyToManyField('Collection', blank=True)
    name = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name_plural = "Taxa"

    class MPTTMeta:
        order_insertion_by = ['name']


class Collection(models.Model):
    """Assign content to collections and collections to taxa.
        -content in multiple containers assigned to taxa will show duplicates.
    """
    name = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Attachment(models.Model):
    recipients = models.ManyToManyField('Content', blank=True)
    name = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name
