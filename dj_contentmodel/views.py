# -*- coding: utf-8 -*-
"""
Example views.
    -Don't use these in production.
    -URL schemas and slugified routes not yet implemented.
    -Refactor as class based views.
"""
from django.shortcuts import render_to_response, RequestContext
from .models import Sitemap


def get_navigation_tree(request, group=None):
    if group == None:
        nodes = Sitemap.objects.all()
    else:
        nodes = Sitemap.objects.filter(groups=group)
    templatePath = "dj_contentmodel/sitemap.html"
    return render_to_response(templatePath, {'nodes': nodes}, context_instance=RequestContext(request))


def get_content_tree(request, group=None):
    if group == None:
        nodes = Sitemap.objects.all()
    else:
        nodes = Sitemap.objects.filter(groups=group)
    templatePath = "dj_contentmodel/taxonomy.html"
    return render_to_response(templatePath, {'nodes': nodes}, context_instance=RequestContext(request))
