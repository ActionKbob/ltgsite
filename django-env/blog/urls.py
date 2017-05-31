from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url( r'^$', views.index, name = 'blog'  ),
    url(r'^(?P<selected_page>\d+)/?$', views.index, name = 'blog' ),
    url( r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+).html', views.post_view, name = 'view_blog_post' ),
    url( r'^category/(?P<slug>[-\w]+)/?$', views.post_category, name = 'view_blog_category' ),
]
