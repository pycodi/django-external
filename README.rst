=============================
django-external
=============================

.. image:: https://badge.fury.io/py/django-external.svg
    :target: https://badge.fury.io/py/django-external

.. image:: https://travis-ci.org/pycodi/django-external.svg?branch=master
    :target: https://travis-ci.org/pycodi/django-external

.. image:: https://codecov.io/gh/pycodi/django-external/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pycodi/django-external

External system message for Django

Documentation
-------------

The full documentation is at https://django-external.readthedocs.io.

Quickstart
----------

Install django-external::

    pip install django-external

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'external.apps.ExternalConfig',
        ...
    )

Add django-external's URL patterns:

.. code-block:: python

    from external import urls as external_urls


    urlpatterns = [
        ...
        url(r'^', include(external_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
