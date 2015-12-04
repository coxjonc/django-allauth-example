from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, "this_is_a_test/index.html")