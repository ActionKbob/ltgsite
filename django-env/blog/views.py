# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage

def index( request, selected_page = 1 ) :
    posts = Blog.objects.all().order_by( '-created' )
    pages = Paginator( posts, 5 )
    try :
        returned_page = pages.page( selected_page )
    except EmptyPage :
        returned_page = pages.page( pages.num_pages )

    return render_to_response( 'layout/blog/index.html', {
        'categories' : Category.objects.all(),
        'posts' : returned_page.object_list,
        'page' : returned_page,
    } )

def post_view( request, slug, category ) :
    return render_to_response( 'layout/blog/post_view.html', {
        'post' : get_object_or_404( Blog, slug = slug )
    } )

def post_category( request, slug ) :
    category = get_object_or_404( Category, slug = slug )
    return render_to_response( 'layout/blog/index.html', {
        'categories' : Category.objects.all(),
        'posts' : Blog.objects.filter( category = category ).order_by( '-created' )[ :5 ]
    } )
