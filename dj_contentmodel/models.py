# -*- coding: utf-8 -*-
"""
Abstract classes for creating taxonomies.
# Role is the only concrete class.
"""
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from taggit.managers import TaggableManager


class Role(MPTTModel):
    """Authentication and authorization has not been implemented.
    # This is feigned through querying groups for now.
    # Template queries for all taxa assigned to a group.
    """
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        app_label = 'dj_contentmodel'


    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


class AbstractTaxonomy(MPTTModel):
    """Inherit from Taxonomy to create taxa.
    # Define collections attribute in subclass.
    """
    groups = TreeManyToManyField('Role')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        app_label = 'dj_contentmodel'
        verbose_name_plural = "Category"
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name



class AbstractCollection(models.Model):
    """Assign content to collections and collections to taxa.
    # Content in multiple containers assigned to taxa will display duplicates.
    """
    name = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        app_label = 'dj_contentmodel'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractContent(models.Model):
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        app_label = 'dj_contentmodel'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractAttachment(models.Model):
    '''Assign attachments to subclass of AbstractContent.
    # Define parents attribute in subclass.
    '''
    name = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        app_label = 'dj_contentmodel'
        ordering = ['name']

    def __unicode__(self):
        return self.name
