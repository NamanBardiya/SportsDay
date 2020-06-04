from django.urls import path
from . import views

urlpatterns = [
    path('',views.Admin, name='Admin'),
    path('add',views.add, name='add'),
]