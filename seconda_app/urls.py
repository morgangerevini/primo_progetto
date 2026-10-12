from django.urls import path
from seconda_app.views import *

app_name = 'seconda_app'
urlpatterns = [
    path('es_if', esempio_if, name = 'es_if'),
    path('if-else-elif', if_else_elif, name = 'if_else_elif'),
    path('es_for', esempio_for, name = 'es_for')
]