import pytz

from django.utils import timezone

class TimezoneMiddleware:
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

        print(timezone.get_current_timezone_name())
