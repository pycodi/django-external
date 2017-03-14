=====
Usage
=====

To use django-external in a project, add it to your `INSTALLED_APPS`:

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
