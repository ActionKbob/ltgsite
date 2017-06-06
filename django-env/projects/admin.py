# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from projects.models import Project, Category, ProjectImage

class ProjectImageInline( admin.TabularInline ):
    model = ProjectImage
    extra = 3

class ProjectAdmin( admin.ModelAdmin ) :
    list_display = ( 'name', 'created' )
    exclude = [ 'created' ]
    prepopulated_fields = { 'slug' : ( 'name', ) }
    inlines = [ ProjectImageInline, ]

class CategoryAdmin( admin.ModelAdmin ) :
    prepopulated_fields = { 'slug' : ( 'title', ) }

admin.site.register( Project, ProjectAdmin )
admin.site.register( Category, CategoryAdmin )
