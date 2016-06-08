# -*- coding: utf-8 -*-
"""
Group is the only required AdminManager.
    -If Sitemap, Collection, or Page models are removed, unregistered their admins.
"""
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Group, Sitemap, Collection, Page

admin.site.register(
    Group,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)


admin.site.register(
    Sitemap,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Collection)
admin.site.register(Page)
