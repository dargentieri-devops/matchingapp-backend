from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    response = ""
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)
    elif request.method == 'GET':
        if "val" in request.GET:
            response=request.GET['val']
    return HttpResponse("Hello, world. You're at the matchinapp index."+response)
