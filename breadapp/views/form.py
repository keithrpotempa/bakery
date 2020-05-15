import sqlite3
from django.shortcuts import render
from .details import get_bread
from ..models import Bread, model_factory
from ..connection import Connection

def bread_form(request):
    if request.method == 'GET':
        template = 'breads/form.html'
        context = {
          
        }
        
        return render(request, template, context)
    
def bread_edit_form(request, bread_id):
    if request.method == 'GET':
        bread = get_bread(bread_id)
        
        template = 'breads/form.html'
        context = {
            'bread': bread
        }
        
        return render(request, template, context)