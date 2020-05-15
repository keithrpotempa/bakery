import sqlite3
from django.shortcuts import render
from ..models import Bread, model_factory
from ..connection import Connection

def bread_form(request):
    if request.method == 'GET':
        template = 'breads/form.html'
        context = {
          
        }
        
        return render(request, template, context)