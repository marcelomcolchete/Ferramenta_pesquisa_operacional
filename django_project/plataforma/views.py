from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .forms import (
	AlgoritmoGrafico
	)

def home(request):
	data = {}
	data['active'] = "home"
	if request.method == 'POST':
		funcao_objetivo_tipo 	= request.POST.get('funcao_objetivo_tipo')
		funcao_objetivo_x1 		= request.POST.get('funcao_objetivo_x1')
		funcao_objetivo_x2 		= request.POST.get('funcao_objetivo_x2')
		restricao1_x1 			= request.POST.get('restricao1_x1')
		restricao1_x2 			= request.POST.get('restricao1_x2')
		print(funcao_objetivo_tipo)
		print(funcao_objetivo_x1)
		print(funcao_objetivo_x2)
		print(restricao1_x1)
		print(restricao1_x2)
	data['form'] = AlgoritmoGrafico()
	return render(request, 'plataforma/index.html', data)