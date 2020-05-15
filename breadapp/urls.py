from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
      path('', bread_list, name='breads'),
      path('breads/', bread_list, name='breads'),
      path('form/', bread_form, name='bread_form'),
      path('breads/<int:bread_id>', bread_details, name='bread')
]
