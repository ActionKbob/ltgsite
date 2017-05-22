from django.conf.urls import url, include
from layout import views

urlpatterns = [
    url( r'^$', views.index, name = 'index' ),
]

handler404 = 'layout.views.handler404'
