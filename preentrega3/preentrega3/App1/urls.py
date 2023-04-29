from django.urls import path
from App1 import views

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('guitarras', views.guitarras, name='guitarras'),
    path('guitarrasInfo', views.guitarrasInfo, name='guitarrasinfo'),
    path('guitarrasFormulario', views.guitarrasFormulario, name='guitarrasformulario'),
    path('busquedaInstrumento',views.busquedaInstrumento,name="busquedainstrumento"),
    path('buscar/',views.buscar),
]