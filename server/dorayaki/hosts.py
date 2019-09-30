from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(\w+)', 'dorayaki.urls', name='api'),
    # host(r'api', 'dorayaki.urls', name='api'),
    # host(r'beta', 'beta.urls', name='beta'),
)