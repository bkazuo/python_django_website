# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Render always look for a folder called templates
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/basic.html', {'content': ['If you would like to contact me, plase email me','teste@teste.com']}) # Passing a dict to the render html file