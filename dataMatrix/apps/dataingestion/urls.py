from django.urls import path
from . import views


urlpatterns = [
    path('dataingestion/csvingest/', views.csvingest, name='csvingest'),
    path('dataingestion/fileingest/', views.fileingest, name='fileingest')
    ]