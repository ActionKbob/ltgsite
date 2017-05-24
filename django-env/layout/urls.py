from django.conf.urls import url, include
from layout import views

urlpatterns = [
    url( r'^$', views.index, name = 'index' ),
    url( r'^style_guide', views.style_guide, name = 'style guide' ),
]

handler404 = 'layout.views.handler404'
