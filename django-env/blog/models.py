# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

class Blog( models.Model ) :
    title = models.CharField( max_length = 100, unique = True )
    slug = models.SlugField( max_length = 100, unique = True )
    author = models.ForeignKey( 'about.member' )
    body = models.TextField()
    created = models.DateTimeField( db_index = True, auto_now_add = True )
    category = models.ForeignKey( 'blog.category' )
    keywords = models.CharField( max_length = 100 )
    featuredImage = models.ImageField( upload_to = 'images/featured/%Y/%m/%d', max_length = 100, blank=True, null=True )
    posted = models.BooleanField( default = False )

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

    def __str__( self ) :
        return self.title
