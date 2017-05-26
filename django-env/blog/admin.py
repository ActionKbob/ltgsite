# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin( admin.ModelAdmin ) :
    list_display = ( 'title', 'author', 'created', 'posted' )
    exclude = [ 'created' ]
    prepopulated_fields = { 'slug' : ( 'title', ) }

class CategoryAdmin( admin.ModelAdmin ) :
    prepopulated_fields = { 'slug' : ( 'title', ) }

admin.site.register( Blog, BlogAdmin )
admin.site.register( Category, CategoryAdmin )
