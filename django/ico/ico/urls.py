"""ico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns = [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    
    path('', views.home, name='home'),
    
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('accounts.urls')),
    path('console/', include('console.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


