from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # Service worker must be served from the site root so its scope covers '/'
    path('sw.js', TemplateView.as_view(template_name='sw.js',
                                       content_type='application/javascript')),
    # Digital Asset Links — lets the Play Store TWA app claim this site
    path('.well-known/assetlinks.json',
         TemplateView.as_view(template_name='assetlinks.json',
                              content_type='application/json')),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'),
         name='privacy'),
    path('', include('practice.urls')),
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
]
