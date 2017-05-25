# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from about.models import Member

class MemberAdmin( admin.ModelAdmin ) :
    list_display = ( 'first_name', 'last_name', 'title' )

admin.site.register( Member, MemberAdmin )
