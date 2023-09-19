from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'api', 'rest_api.urls', name='api'),
    host(r'helpdesk', 'helpdesk.urls', name='helpdesk'),
)