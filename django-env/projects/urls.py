from django.conf.urls import url, include
from projects import views

urlpatterns = [
    url( r'^$', views.index, name = 'projects'  )
]
