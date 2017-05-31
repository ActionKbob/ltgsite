# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

class Project( models.Model ) :
    name = models.CharField( max_length = 100, unique = True )
    slug = models.SlugField( max_length = 100, unique = True )
    category = models.ForeignKey( 'projects.category' )
    body = models.TextField()
    description = models.TextField()
    created = models.DateTimeField( db_index = True, auto_now_add = True )
    keywords = models.CharField( max_length = 100 )

    def __unicode__( self ) :
        return '%s' % self.title

    @permalink
    def get_absolute_url( self ) :
        return( 'view_project_post', None, { 'slug' : self.slug, 'category' : self.category.slug } )

class Category( models.Model ) :
    title = models.CharField( max_length = 100, unique = True )
    slug = models.SlugField( max_length = 100, unique = True )

    def __unicode__( self ) :
        return '%s' % self.title

    @permalink
    def get_absolute_url( self ) :
        return( 'view_project_category', None, { 'slug' : self.slug } )

    def __str__( self ) :
        return self.title
