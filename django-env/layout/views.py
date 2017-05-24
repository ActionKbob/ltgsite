from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index( request ) :
    return render_to_response( 'layout/index.html', {} )

def style_guide( request ) :
    return render_to_response( 'layout/style_guide.html', {} )
