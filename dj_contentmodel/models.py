# -*- coding: utf-8 -*-
"""
Example sitemap. These can be refactored as needed.
"""
from __future__ import unicode_literals
from .abstracts import *


class Sitemap(Taxonomy):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Sitemap"


class Collection(Collection):
    contents = models.ManyToManyField('Page', blank=True)


class Page(Content):
    body = models.TextField(blank=True, null=True)
