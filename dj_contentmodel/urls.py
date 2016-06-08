# -*- coding: utf-8 -*-
"""
Example navigation.
    -Don't use these in production.
    -URL schemas and slugified routes not yet implemented.
"""
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^navigation/(?P<group>[0-9]+)?$', views.get_navigation_tree),
    url(r'^sitemap/(?P<group>[0-9]+)?$', views.get_content_tree),
]
