from django.conf.urls import url, include
from projects import views

urlpatterns = [
    url( r'^$', views.index, name = 'projects'  ),
    url( r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+).html', views.post_view, name = 'view_project_post' ),
]
