from django.urls import path
from products.views import  *





urlpatterns = [
     path('Lista-Productos/', Listaproductos, name='Productos'),
     path('Carga-Procesador/', cargarProcesador, name='procesador'),
     path('Carga-Placa/', cargarPlacaMadre, name='placa'),
     path('Carga-Ram/', cargarRam, name='ram'),
     path('lista-Procesador/', listarProcesador, name='listaProcesador'),
     path('lista-Placa/', listarPlacaMadre, name='listaPlaca'),
     path('lista-Ram/', listarRam, name='listaRam'),
     path('buscar-Procesador/',busca_Procesador, name= 'buscaprocesador'),# type: ignore  
     path('buscar-Placa/',busca_Placa, name= 'buscaplaca'),# type: ignore  
     path('buscar-Ram/',busca_ram, name= 'buscaram'),# type: ignore  
]
