from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def index( request ) :
    return render_to_response( 'layout/index.html', {} )
