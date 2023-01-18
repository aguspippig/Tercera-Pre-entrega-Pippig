
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from products.models import Procesador, PlacaMadre, Ram
from products.forms import *



def cargaProductos(request):
    return render(request=request,
                  template_name='products/cargaproductos.html',
                  )


def Listaproductos(request):

    return render(request=request,
                  template_name='products/lista-productos.html',
                  )


def listarProcesador(request):
    contexto = {
        'procesadores': Procesador.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaProcesador.html',
                  context=contexto,
                  )


def listarPlacaMadre(request):
    contexto = {
        'placas_madres': PlacaMadre.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaPlaca.html',
                  context=contexto,
                  )


def listarRam(request):
    contexto = {
        'ram': Ram.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaRam.html',
                  context=contexto,
                  )


def cargarProcesador(request):
    if request.method == 'POST':
        formulario = CargaProcesador(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            procesador = Procesador(
                              marca=data['marca'],
                              modelo=data['modelo'],
                              stock=data['stock'],
                              )
            procesador.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaProcesador()
    return render(
        request=request,
        template_name='products/cargaProcesador.html',
        context={'formulario': formulario},
    )


def cargarPlacaMadre(request):
    if request.method == 'POST':
        formulario = CargaPlacaMadre(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            placa = PlacaMadre(
                            marca=data['marca'],
                            modelo=data['modelo'],
                            stock=data['stock'],
                            )
            placa.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaPlacaMadre()
    return render(
        request=request,
        template_name='products/cargaPlaca.html',
        context={'formulario': formulario},
    )


def cargarRam(request):
    if request.method == 'POST':
        formulario = CargaRam(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            ram = Ram(
                    marca=data['marca'],
                    modelo=data['modelo'],
                    stock=data['stock'],
                          )
            ram.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaRam()
    return render(
        request=request,
        template_name='products/cargaRam.html',
        context={'formulario': formulario},
    )



def busca_ram(request):
    if request.method == "POST":
        data = request.POST
        ram = Ram.objects.filter(
            Q(modelo__contains=data['modelo']) 
        )
 
        contexto = {
            'Ram': ram
        }
        return render(
            request=request,
            template_name='products/listaRam.html',
            context=contexto,
        )

def busca_Procesador(request):
    if request.method == "POST":
        data = request.POST
        procesador = Procesador.objects.filter(
            Q(modelo__contains=data['modelo']) 
        )
        contexto = {
            'Procesadores': procesador
        }
        return render(
            request=request,
            template_name='products/listaProcesador.html',
            context=contexto,
        )
        
def busca_Placa(request):
    if request.method == "POST":
        data = request.POST
        placa=PlacaMadre.objects.filter(
            Q(modelo__contains=data['modelo']) 
        )
        contexto = {
            'Placas Madres': placa
        }
        return render(
            request=request,
            template_name='products/listaPlaca.html',
            context=contexto,
        )
    
