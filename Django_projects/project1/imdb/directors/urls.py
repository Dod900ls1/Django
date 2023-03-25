from django.urls import path
from . import views

app_name = 'lib'

urlpatterns = [
    # http://127.0.0.1:8000/imdb
    path('', views.index, name='index')
]