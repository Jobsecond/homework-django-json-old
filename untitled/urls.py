# -*- coding: utf-8 -*-
"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
from django.conf.urls import url
from django.contrib import admin
#from django.views.generic import TemplateView
from django.views.static import serve
from myapp.views import login, display, Add, manage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name="login"),
    url(r'^add/', Add, name="add"),# TemplateView.as_view(template_name="login.html")),
    #url(r'^delete/(\d+)/$', delete, name="delete"),
    #url(r'^modify/(\d+)/$', modify, name="modify"),
    url(r'^manage/', manage, name="manage"),
    url(r'^$', display),
    url(r'^ustatic/(?P<path>.*)$', serve,
        {'document_root': sys.path[0].replace('\\', '/') + '/templates/static'}),
]
