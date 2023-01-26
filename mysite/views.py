from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    #return HttpResponse(render(request,'default.html'))
    return HttpResponse(render(request,'index.html'))

def about(request):
    template_name = 'about.html'
    return HttpResponse(render(request,'about.html'))

def contacts(request):
    template_name = 'contacts.html'
    return HttpResponse(render(request,'contacts.html'))