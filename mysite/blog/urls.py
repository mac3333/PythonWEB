from django.urls import path, include
from . import views



urlpatterns = [
    
    path('', views.home, name="home"),
    path('producto/', views.producto, name="producto"),
    path('pedidos/<str:id_producto>/', views.pedidos, name="pedidos"),
    path('register/',views.register, name="register"),
    path('buscar/',views.buscar),
    path('contacto/',views.contacto, name="contacto"),
    
    
  
    
    
   



]
