# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index( request ) :
    return render_to_response( 'layout/blog/index.html', {
        'categories' : Category.objects.all(),
        'posts' : Blog.objects.all()[ :5 ]
    } )

def post_view( request, slug ) :
    return render_to_response( 'layout/blog/post_view.html', {
        'post' : get_object_or_404( Blog, slug = slug )
    } )

def post_category( request, slug ) :
    category = get_object_or_404( Category, slug = slug )
    return render_to_response( 'layout/blog/index.html', {
        'categories' : Category.objects.all(),
        'posts' : Blog.objects.filter( category = category )[ :5 ]
    } )
