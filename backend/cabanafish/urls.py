from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

admin.site.site_header  = 'CABANA FISH — Administration'
admin.site.site_title   = 'CABANA FISH'
admin.site.index_title  = 'Orders & Quotations'

FRONTEND_DIR = settings.BASE_DIR.parent  # CabanaFish root folder

def serve_frontend(request, path='index.html'):
    response = serve(request, path, document_root=FRONTEND_DIR)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quotes.urls')),

    # Serve the frontend (index.html at /, all other files by path)
    # Negative lookahead excludes admin/ and api/ so Django handles them first
    re_path(r'^$',                                      serve_frontend),
    re_path(r'^(?P<path>(?!admin|api).+)$',             serve_frontend),
]
