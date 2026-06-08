from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

admin.site.site_header  = 'CABANA FISH — Administration'
admin.site.site_title   = 'CABANA FISH'
admin.site.index_title  = 'Orders & Quotations'

FRONTEND_DIR = settings.BASE_DIR.parent  # CabanaFish root folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quotes.urls')),

    # Serve the frontend (index.html at /, all other files by path)
    # Negative lookahead excludes admin/ and api/ so Django handles them first
    re_path(r'^$',                                      serve, {'document_root': FRONTEND_DIR, 'path': 'index.html'}),
    re_path(r'^(?P<path>(?!admin|api).+)$',             serve, {'document_root': FRONTEND_DIR}),
]
