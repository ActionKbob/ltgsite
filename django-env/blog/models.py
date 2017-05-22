# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

class Blog( models.Model ) :
    title = models.CharField( max_length = 100, unique = True )
    slug = models.SlugField( max_length = 100, unique = True )
    body = models.TextField()
    posted = models.DateTimeField( db_index = True, auto_now_add = True )
    category = models.ForeignKey( 'blog.category' )
    keywords = models.CharField( max_length = 100 )

    def __unicode__( self ) :
        return '%s' % self.title

    @permalink
    def get_absolute_url( self ) :
        return( 'view_blog_post', None, { 'slug' : self.slug } )

class Category( models.Model ) :
    title = models.CharField( max_length = 100, unique = True )
    slug = models.SlugField( max_length = 100, unique = True )

    def __unicode__( self ) :
        return '%s' % self.title

    @permalink
    def get_absolute_url( self ) :
        return( 'view_blog_category', None, { 'slug' : self.slug } )