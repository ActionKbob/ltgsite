from __future__ import unicode_literals
from about.models import Member
from django.shortcuts import render_to_response, get_object_or_404

def index( request ) :
    return render_to_response( 'layout/about/index.html', {
        'members' : Member.objects.all()
    } )
