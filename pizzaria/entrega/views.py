# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import datetime

from .models import Pizza

class HoraView(TemplateView):
    template_name = 'entrega/hora.html'
    
    def get_context_data(self, **kwargs):
        context = super(HoraView, self).get_context_data(**kwargs)
        context['hora_certa'] = datetime.datetime.now()
        return context

    
def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.all():
        listagem.append(unicode(pizza))
    listagem = u'\n'.join(listagem)
    html = u'<html><body><h1>Pizzas Pendentes</h1>'
    html += u'<pre>{0}</body></html>'.format(listagem)
    return HttpResponse(html)
    
def pizzas_pendentes(request):
    return render(request, 'entrega/pizzas.html'
                         , {"lista": Pizza.objects.all()
                         ,  "hora":datetime.datetime.now()}
                         , content_type="text/html")
                         
def hora_atual_na_unha(request):
    agora = datetime.datetime.now()
    html = '<html><body><h1>Hora atual: {0}</h1></body></html>'.format(agora)
    return HttpResponse(html)
     
