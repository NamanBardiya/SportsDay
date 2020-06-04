from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('rankings',views.rankings,name='rankings'),
    path('filtering',views.filtering,name='filtering'),
]