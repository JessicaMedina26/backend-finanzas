from django.contrib import admin
from django.urls import path
from bancos import views

urlpatterns = [
    path('api/ciudad/', views.CiudadViewSet.as_view({'get': 'list'})),
    path('api/ciudad/create', views.CiudadViewSet.as_view({'post': 'create'})),

    path('api/cliente/', views.ClienteViewSet.as_view({'get': 'list'})),
    path('api/cuentas/', views.CuentaBancariaViewSet.as_view({'get': 'list'})),
    path('api/movimiento/', views.MovimientoViewSet.as_view({'get': 'list'})),
    path('api/operacion', views.OperacionViewSet.as_view({'get': 'list'}))
]
