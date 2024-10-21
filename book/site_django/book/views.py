from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')

class IndexPageView(TemplateView):
    template_name = 'index.html'

def palindromo(request, palabra):
    es_palindromo = ''
    palabra_sin_espacios = palabra.replace(' ', '')   #yohagoyogahoy
    if palabra_sin_espacios == palabra_sin_espacios[::-1] :
        es_palindromo = 'ES PALINDROMO'
    else: # si no lo es
        es_palindromo = 'NO ES PALINDROMO'
    context = {'es_palindromo': es_palindromo, 'palabra': palabra}
    return render(request, 'espalindromo.html', context)
