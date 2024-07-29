from django.urls import path
from . import views

urlpatterns = [
    path('dataManagement/create/', views.createTable, name='createTable'),
    path('dataManagement/delete/', views.deleteTable, name='deleteTable')
]