from django.shortcuts import render,render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from .models import *
import datetime
from django.db.models import Sum
from django.db.models import Q

from .forms import PostForm
from .forms import AddForm
from django.shortcuts import render, get_object_or_404,redirect



def login(request):
    return render(request, 'livrocaixa/TecSoloLogin.html')

def index(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            add = form.save()
            add.save()
        return render(request, 'livrocaixa/index.html', {'form': form})

    else:
        form = AddForm()
        return render(request, 'livrocaixa/index.html', {'form': form})

def post_list(request):
    devendo = Amostra.objects.filter(Pago=False).order_by('Cliente')
    return render(request, 'livrocaixa/post_list.html', {'devendo': devendo})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_fields = ['Cliente', 'Cod_Amostra', 'Valor', 'Propriedade','Gleba', 'Municipio', 'Amostras', 'Data',]
        entry_query = get_query(query_string, search_fields)
        found_entries = Amostra.objects.filter(entry_query)

    return render_to_response('livrocaixa/search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },context_instance=RequestContext(request))

def search_results(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_fields = ['Nome', 'Valor',]
        entry_query = get_query(query_string, search_fields)
        found_entries = Gasto.objects.filter(entry_query)

    return render_to_response('livrocaixa/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },context_instance=RequestContext(request))


def pagos(request):
    pagos = Amostra.objects.filter(Pago=True).order_by('Data')
    return render(request, 'livrocaixa/pagos.html', {'pagos': pagos})

def gastos(request):
    gastos = Gasto.objects.all().order_by('Valor')

    return render(request, 'livrocaixa/gastos.html', {'gastos' : gastos})

def new_gastos(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_gastos = form.save()
            new_gastos.save()
        return render(request, 'livrocaixa/new_gastos.html', {'form': form})

    else:
        form = PostForm()
        return render(request, 'livrocaixa/new_gastos.html', {'form': form})

def amostra_detail(request, pk):
    amostra = get_object_or_404(Amostra, pk=pk)
    return render(request, 'livrocaixa/amostra_detail.html', {'amostra': amostra})

def gasto_detail(request, pk):
        gasto = get_object_or_404(Gasto, pk=pk)
        return render(request, 'livrocaixa/gasto_detail.html', {'gasto': gasto})


def amostra_edit(request, pk):
    amostra = get_object_or_404(Amostra, pk=pk)
    if request.method == "POST":
        form = AddForm(request.POST, instance=amostra)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.save()
            return redirect('livrocaixa.views.amostra_detail', pk=amostra.pk)
    else:
        form = AddForm(instance=amostra)
    return render(request, 'livrocaixa/amostra_edit.html', {'form': form})

def gasto_edit(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=gasto)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.save()
            return redirect('livrocaixa.views.gasto_detail', pk=gasto.pk)
    else:
        form = PostForm(instance=gasto)
    return render(request, 'livrocaixa/gasto_edit.html', {'form': form})


def reducao(request):

    reducao = Amostra.objects.filter(Pago=True).aggregate(Sum('Valor')).get('Valor__sum', 0.00)
    return render(request, 'livrocaixa/reducao.html', {'reducao' : reducao})
