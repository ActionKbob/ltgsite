from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from layout import views

urlpatterns = [
    url( r'^$', views.index, name = 'index' ),
    url( r'^style_guide', views.style_guide, name = 'style guide' ),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

handler404 = 'layout.views.handler404'
