from django.urls import path
from django.conf.urls import  include
from . import views
urlpatterns=[
    path('',views.user,name='User'),
    path('FormularioRegistro/', include('registration.html.urls',namespace="Registro")),
]


