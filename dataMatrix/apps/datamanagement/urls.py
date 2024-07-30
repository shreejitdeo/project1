from django.urls import path
from . import views

urlpatterns = [
    path('datamanagement/create/', views.createTable, name='createTable'),
    path('datamanagement/delete/', views.deleteTable, name='deleteTable')
    ]
