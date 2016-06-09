========
Usage
========
First, install dj-contentmodel::

    pip install dj-contentmodel

Add django-mptt, django-taggit, and dj-contentmodel in INSTALLED_APPS.
::

    INSTALLED_APPS = [
        ...
        'mptt',
        'taggit',
        'dj_contentmodel',
        ...
    ]

Then, import the abstract base classes.::

    from dj_contentmodel.models import Taxonomy, Collection, Content, Attachment

Next, subclass the imported classes to create taxonomies and content models as needed.
The following example is of a minimum configuration.
The names of defined classes are arbitrary, but the relationships among classes are not.
::

    class Sitemap(Taxonomy):
        """Main navigation"""
        collections = models.ManyToManyField('Bucket', blank=True)
        class Meta:
            verbose_name = "Category"
            verbose_name_plural = "Categories"
        ...

    class Bucket(Collection):
        """Arbitrary collections to group content."""
        contents = models.ManyToManyField('Page', blank=True)
        ...

    class Page(Content):
        ...

    class Report(Attachment):
        parents = models.ManyToManyField('Page', blank=True)
        ...

After creating your models register the subclass of Taxonomy using
DraggableMPTTAdmin. Collection, Content, and Attachment subclasses do
not require customization.
::

    from django.contrib import admin
    from mptt.admin import DraggableMPTTAdmin
    from .models import Sitemap, Collection, Page
    admin.site.register(
        Sitemap,
        DraggableMPTTAdmin,
        list_display=(
            'tree_actions',
            'indented_title',),
        list_display_links=(
            'indented_title',),)
    admin.site.register(Bucket)
    admin.site.register(Page)
    admin.site.register(Report)

Without a migration, it may be necessary to create the tables using syncdb.
::

    python manage.py migrate --run-syncdb


Once a taxonomy is defined and registered in the admin, create your views.
For simplicity, funtional views are shown here but class based views are preferred.
Until authentication and authorization are implemented, you may filter taxonomies
by group to feign authorization but this is not secure.
::

    from django.shortcuts import render_to_response, RequestContext
    from .models import Sitemap


    def get_content_tree(request, group=None):
        if group == None:
            nodes = Sitemap.objects.all()
        else:
            nodes = Sitemap.objects.filter(groups=group)
        templatePath = "dj_contentmodel/taxonomy.html"    #use navigation.html to omit content nodes
        return render_to_response(templatePath, {'nodes': nodes}, context_instance=RequestContext(request))

Then, create your urls.
::

    urlpatterns = [
        url(r'^navigation/(?P<group>[0-9]+)?$', views.get_navigation_tree),
        url(r'^sitemap/(?P<group>[0-9]+)?$', views.get_content_tree),
    ]

Finally, create a template from the templates provided.

Sitemap.
::

    {% load mptt_tags %}
    {% load staticfiles %}
    <ul>
        {% recursetree nodes %}
            <li>
                <a href="{% url 'app:url' %}{{ node.id }}">{{ node.name }}</a>
                    {% if not node.is_leaf_node %}
                        <ul class="children">
                            {{ children }}
                        </ul>
                    {% endif %}
            </li>
        {% endrecursetree %}
    </ul>


Sitemap and associated content. Additional tags are provided by
django-mptt and django-taggit.Note that content assigned to multiple collections
associated with the same taxa will display duplicate content.
::

    {% load mptt_tags %}
    <ul>
        {% recursetree nodes %}
            <li>
                <a href="{% url 'app:url' %}{{ node.id }}">{{ node.name }}</a>
                {% if not node.is_leaf_node %}
                    <ul class="children">
                        {{ children }}
                    </ul>
                {% endif %}
                {% if node.collections.contents.count > 0 %}
                    <ul>
                        {% for content in node.collections.contents.prefetch_related %}
                            <li><a href="{% url 'app:url' %}{{ content.id }}">{{ content.name }}</a></li>
                        {% endfor %}
                    </ul>
                {% endif %}
            </li>
        {% endrecursetree %}
    </ul>
