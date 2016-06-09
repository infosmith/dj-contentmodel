=============================
dj-contentmodel
=============================


Boilerplate for taxonomies, content collections, and content models using django-mptt and django-taggit.

Features
--------
* Drag and drop construction of taxonomies.
* Arbitrary relationships among groups, taxonomies, collections, content, and attachments.
* Templates for displaying taxonomies with and without collections' contents.

Documentation
-------------
dj-content model is just boilerplate for django-mptt and django-taggit.
It defines a hierarchical structure with arbitrary relationships via collections.
The Quickstart example is a sufficient starting point for many projects.
Each abstract class provided by dj-contentmodel is a descendant of django.db.models, so
extend them as you would a Django model. The Group and Taxonomy classes are also
descendants of django-mptt's MPTTModel class and can be extended accordingly.
Additional examples dj-contentmodel's abstract classes are available at https://dj-contentmodel.readthedocs.org.

Quickstart
----------
First, install dj-contentmodel::

    pip install dj-contentmodel

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
Finally, register your models with the admin.::

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
Without a migration, it may be necessary to create the tables.::

    python manage.py migrate --run-syncdb


Running Tests
--------------

Does the code actually work? For now I have my fingers crossed.
Later iterations will be test driven and include integration and performance testing.
::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  `django-mptt`_
*  `django-taggit`_
*  `pip-tools`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`django-mptt`: https://github.com/django-mptt/django-mptt
.. _`django-taggit`: https://github.com/alex/django-taggit
.. _`pip-tools`: https://github.com/nvie/pip-tools
