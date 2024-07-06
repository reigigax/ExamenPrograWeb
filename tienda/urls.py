#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   
    path('base', views.base, name="base"),
    path('contacto', views.base, name="contacto"),
    path('nosotros',views.nosotros, name="nosotros"),
]