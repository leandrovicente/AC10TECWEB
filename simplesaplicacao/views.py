from django.shortcuts import render
# Create your views here.
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.template import Template, Context
# from forms import LoginForm

def home(request):
        return render(request,'index.html')

'''
class Lista(ListView):
        template_name = 'lista.html'
        context_object = 'nome'
        fields = "__all__" 
'''
def cadastroAluno(request):
        context = {
        
    }
    return render(request, 'cadastroAluno.html', context)



def cadastroDisciplina(request):
        context = {
        
    }
    return render(request, 'cadastroDisciplina.html', context)


def cadastroProfessor(request):
        context = {
        
    }
    return render(request, 'cadastroProfessor.html', context)
