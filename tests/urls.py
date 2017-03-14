# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from external.urls import urlpatterns as external_urls

urlpatterns = [
    url(r'^', include(external_urls, namespace='external')),
]
