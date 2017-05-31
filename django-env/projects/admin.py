# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from projects.models import Project, Category

class ProjectAdmin( admin.ModelAdmin ) :
    list_display = ( 'name', 'created' )
    exclude = [ 'created' ]
    prepopulated_fields = { 'slug' : ( 'name', ) }

class CategoryAdmin( admin.ModelAdmin ) :
    prepopulated_fields = { 'slug' : ( 'title', ) }

admin.site.register( Project, ProjectAdmin )
admin.site.register( Category, CategoryAdmin )
