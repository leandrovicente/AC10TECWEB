"""projetoaula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Definindo a url do projeto. Abra o arquivo urls.py
from simplesaplicacao import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# from forms import LoginForm



admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^lista/$', views.Lista.as_view(), name='lista'),
    url(r'^lista/$', views.cadastroAluno, name='cadastroAluno'),  
    # url(r'^teste/$', views.Teste, name='teste'),
    url(r'^lista/$', views.cadastroDisciplina, name='cadastroDisciplina')
    url(r'^lista/$', views.cadastroProfessor, name='cadastroProfessor') 
]   

