from django.db.models import F
from .models import Newstats


class AnalysisMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        ua = request.META.get('HTTP_USER_AGENT', '')

        ignored_prefixes = ['/admin', '/static', '/media', '/.well-known']
        is_ignored = any(path.startswith(p) for p in ignored_prefixes)

        if not is_ignored and ua:
            self.get_device(ua)

        response = self.get_response(request)
        return response
    
    def get_device(self, os_info):
        if 'iPhone' in os_info:
            Newstats.objects.update(iphone=F('iphone') + 1)
        elif 'Android' in os_info:
            Newstats.objects.update(android=F('android') + 1)
        elif 'Windows' in os_info:
            Newstats.objects.update(win=F('win') + 1)
        elif 'Macintosh' in os_info:
            Newstats.objects.update(mac=F('mac') + 1)
        else:
            Newstats.objects.update(others=F('others') + 1)
