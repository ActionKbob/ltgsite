from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url( r'^$', views.index, name = 'blog'  ),
    url( r'^view/(?P<slug>[^\.]+).html', views.post_view, name = 'view_blog_post' ),
    url( r'^category/(?P<slug>[^\.]+).html', views.post_category, name = 'view_blog_category' ),
]
