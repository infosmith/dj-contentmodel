
# -*- coding: utf-8 -*-
"""
Abstract classes for creating taxonomies.
-Group is the only concrete class
"""
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from taggit.managers import TaggableManager


class Group(MPTTModel):
    """Authentication and authorization has not been implemented.
        -This is feigned through querying groups for now.
        -Template queries for all taxa assigned to a group.
    """
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


class Taxonomy(MPTTModel):
    """Inherit from Taxonomy to create taxa."""
    groups = TreeManyToManyField('Group')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    collections = models.ManyToManyField('Collection', blank=True)
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        verbose_name_plural = "Taxa"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


class Collection(models.Model):
    """Assign content to collections and collections to taxa.
        -content in multiple containers assigned to taxa will display duplicates.
    """
    name = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Attachment(models.Model):
    recipients = models.ManyToManyField('Content', blank=True)
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return self.name
