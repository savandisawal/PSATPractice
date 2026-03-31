import time
from collections import defaultdict
from django.http import HttpResponse
from django.conf import settings


# Simple in-memory store: {ip: [timestamp, ...]}
_login_attempts = defaultdict(list)


class LoginRateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_attempts = getattr(settings, 'LOGIN_RATE_LIMIT', 5)
        self.window = getattr(settings, 'LOGIN_RATE_WINDOW', 300)

    def __call__(self, request):
        if request.path == '/accounts/login/' and request.method == 'POST':
            ip = self._get_ip(request)
            now = time.time()
            attempts = _login_attempts[ip]
            # Remove old attempts outside the window
            attempts[:] = [t for t in attempts if now - t < self.window]
            if len(attempts) >= self.max_attempts:
                wait = int(self.window - (now - attempts[0]))
                return HttpResponse(
                    f'Too many login attempts. Please wait {wait} seconds.',
                    status=429,
                    content_type='text/plain',
                )
            attempts.append(now)
        return self.get_response(request)

    def _get_ip(self, request):
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded:
            return forwarded.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR', '0.0.0.0')
