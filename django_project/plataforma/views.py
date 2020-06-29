from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

def home(request):
	data = {}
	data['active'] = "home"
	return render(request, 'plataforma/index.html', data)