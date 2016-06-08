=============================
dj-contentmodel
=============================


Pluggable app for hierarchical taxonomies, content collections, and navigation.

Documentation
-------------

The full documentation is at https://dj-contentmodel.readthedocs.org.

Quickstart
----------

Install dj-contentmodel::

    pip install dj-contentmodel

Create initial content model tables if Sitemap, Collection, and Page
will be used.

    python manage.py migrate --run-syncdb

Then use it in a project::

    import dj_contentmodel

Features
--------

* TODO

Running Tests
--------------

Does the code actually work? For now, I've got my fingers crossed. Later iterations will be
test driven including unit, integration, and performance testing.

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
