# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Group,
	Taxonomy,
	Collection,
	Content,
	Attachment,
	Sitemap,
	Page,
)


class GroupCreateView(CreateView):

    model = Group


class GroupDeleteView(DeleteView):

    model = Group


class GroupDetailView(DetailView):

    model = Group


class GroupUpdateView(UpdateView):

    model = Group


class GroupListView(ListView):

    model = Group


class TaxonomyCreateView(CreateView):

    model = Taxonomy


class TaxonomyDeleteView(DeleteView):

    model = Taxonomy


class TaxonomyDetailView(DetailView):

    model = Taxonomy


class TaxonomyUpdateView(UpdateView):

    model = Taxonomy


class TaxonomyListView(ListView):

    model = Taxonomy


class CollectionCreateView(CreateView):

    model = Collection


class CollectionDeleteView(DeleteView):

    model = Collection


class CollectionDetailView(DetailView):

    model = Collection


class CollectionUpdateView(UpdateView):

    model = Collection


class CollectionListView(ListView):

    model = Collection


class ContentCreateView(CreateView):

    model = Content


class ContentDeleteView(DeleteView):

    model = Content


class ContentDetailView(DetailView):

    model = Content


class ContentUpdateView(UpdateView):

    model = Content


class ContentListView(ListView):

    model = Content


class AttachmentCreateView(CreateView):

    model = Attachment


class AttachmentDeleteView(DeleteView):

    model = Attachment


class AttachmentDetailView(DetailView):

    model = Attachment


class AttachmentUpdateView(UpdateView):

    model = Attachment


class AttachmentListView(ListView):

    model = Attachment


class SitemapCreateView(CreateView):

    model = Sitemap


class SitemapDeleteView(DeleteView):

    model = Sitemap


class SitemapDetailView(DetailView):

    model = Sitemap


class SitemapUpdateView(UpdateView):

    model = Sitemap


class SitemapListView(ListView):

    model = Sitemap


class PageCreateView(CreateView):

    model = Page


class PageDeleteView(DeleteView):

    model = Page


class PageDetailView(DetailView):

    model = Page


class PageUpdateView(UpdateView):

    model = Page


class PageListView(ListView):

    model = Page

