import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..models import Bread, Ingredient, model_factory
from ..connection import Connection

def get_bread(bread_id):
  
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bread)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
              b.id,
              b.name,
              b.region
            FROM breadapp_bread b
            WHERE b.id = ?;
        """, (bread_id,))
        
        return db_cursor.fetchone()

def get_bread_ingredients(bread_id):
  
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_bread_ingredient
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
          SELECT
            i.name,
            bi.amount
          FROM breadapp_ingredient i
          JOIN breadapp_breadingredient bi ON bi.ingredient_id = i.id
          WHERE bi.bread_id = ?;
        """, (bread_id,))
        
        return db_cursor.fetchall()

def create_bread_ingredient(cursor, row):
    _row = sqlite3.Row(cursor, row)

    ingredient = Ingredient()
    ingredient.name = _row["name"]
    ingredient.amount = _row["amount"]

    return ingredient

def bread_details(request, bread_id):
    if request.method == 'GET':
        bread = get_bread(bread_id)
        ingredients = get_bread_ingredients(bread_id)
        
        template = 'breads/details.html'
        context = {
          'bread': bread,
          'ingredients': ingredients
        } 
        
        return render(request, template, context)