from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')

class IndexPageView(TemplateView):
    template_name = 'index.html'

    
