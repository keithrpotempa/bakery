import sqlite3
from django.shortcuts import render
from ..models import Bread, model_factory
from ..connection import Connection

def bread_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Bread)
            db_cursor = conn.cursor()

            db_cursor.execute("""
              SELECT
                b.id,
                b.name,
                b.region
              FROM breadapp_bread b
              ORDER BY name ASC;
            """)

            all_breads = db_cursor.fetchall()
      
      
        template = 'bread_list.html'
        context = {
          "all_breads": all_breads,
        }

        return render(request, template, context)
