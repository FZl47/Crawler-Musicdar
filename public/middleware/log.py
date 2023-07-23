from django.conf import settings
from django.http import HttpResponse
from public.models import Log


class LogErrorCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allow_urls = settings.LOG_CONFIG.get('allow_urls',[])
        if any([url.find(request.path) != -1 for url in allow_urls]):
            err_stop_count = int(settings.LOG_CONFIG.get('error_level_stop',5))
            err_logs = Log.objects.filter(level='ERROR',is_checked=False)
            if err_logs.count() > err_stop_count:
                return HttpResponse('Please Check Logs -l ERROR')
        response = self.get_response(request)
        return response
