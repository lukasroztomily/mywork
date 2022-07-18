
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

    
class ForceDefaultLanguageMiddleware(MiddlewareMixin):
    """
    Ignore Accept-Language HTTP headers
    
    This will force the I18N machinery to always choose settings.LANGUAGE_CODE
    as the default initial language, unless another one is set via sessions or cookies
    
    Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
    namely django.middleware.locale.LocaleMiddleware
    """
    def process_request(self, request):
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']

from contextlib import suppress

from django.conf import settings


def inject_accept_language(get_response):
    """
    Ignore Accept-Language HTTP headers.

    This will force the I18N machinery to always choose

      - Ukrainian for the main site
      - ADMIN_LANGUAGE_CODE for the admin site

    as the default initial language unless another one is set via
    sessions or cookies.

    Should be installed *before* any middleware that checks
    request.META['HTTP_ACCEPT_LANGUAGE'], namely
    `django.middleware.locale.LocaleMiddleware`.
    """
    admin_lang = getattr(settings, 'ADMIN_LANGUAGE_CODE',
                         settings.LANGUAGE_CODE)

    def middleware(request):
        # Force Ukrainian locale for the main site
        lang = admin_lang if request.path.startswith('/admin') else 'de'
        accept = request.META.get('HTTP_ACCEPT_LANGUAGE', []).split(',')

        with suppress(ValueError):
            # Remove `lang` from the HTTP_ACCEPT_LANGUAGE to avoid duplicates
            accept.remove(lang)

        accept = [lang] + accept
        request.META['HTTP_ACCEPT_LANGUAGE'] = f"""{','.join(accept)}"""
        return get_response(request)

    return middleware

from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
class LocaleMiddleware(MiddlewareMixin):
    """
    This is a very simple middleware that parses a request
    and decides what translation object to install in the current
    thread context. This allows pages to be dynamically
    translated to the language the user desires (if the language
    is available, of course).
    """

    def process_request(self, request):
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        translation.deactivate()
        return response