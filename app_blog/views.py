from django.http import HttpResponse
from django.shortcuts import render
from app_blog.models import Obra_arq, Inst_edu, Bibliografia
from app_blog.forms import obras_arq_view_form, Inst_edu_form, Bibliografia_form
from django.http import HttpResponse

# Create your views here.
def obras_arq_view(request):
    obras= Obra_arq.objects.all()
    context = {'obras':obras}
    return render(request,'obras_arq.html',context=context)

def inst_edu_view(request):
    instituciones= Inst_edu.objects.all()
    context = {'instituciones':instituciones}
    return render(request,'inst_edu.html',context=context)

def bibliografia_view(request):
    libros = Bibliografia.objects.all()
    context = {'libros':libros}
    return render(request,'bibliografia.html',context=context)

def cargar_obra(request):
    if request.method == 'GET':
        form = obras_arq_view_form()
        context = {'form':form}
        return render(request,'cargar_obra.html',context=context)
    else:
        form = obras_arq_view_form(request.POST)
        if form.is_valid():
            new_obra = Obra_arq.objects.create(
                nombre_obra = form.cleaned_data['nombre_obra'],
                autor_obra = form.cleaned_data['autor_obra'],
                ubicacion_obra = form.cleaned_data['ubicacion_obra'],
                año = form.cleaned_data['año'],
                tipo = form.cleaned_data['tipo'],
            )
            context = {'new_obra':new_obra}
        return render(request,'cargar_obra.html',context=context)

def cargar_Instedu(request):
    if request.method == 'GET':
        form = Inst_edu_form()
        context = {'form':form}
        return render(request,'cargar_instedu.html',context=context)
    else:
        form = Inst_edu_form(request.POST)
        if form.is_valid():
            new_inst = Inst_edu.objects.create(
                nombre_inst = form.cleaned_data['nombre_inst'],
                ubicacion_inst = form.cleaned_data['ubicacion_inst'],
            )
            context = {'new_inst':new_inst}
        return render(request,'cargar_instedu.html',context=context)

def cargar_bibliografia(request):
    if request.method == 'GET':
        form = Bibliografia_form()
        context = {'form':form}
        return render(request,'cargar_biblio.html',context=context)
    else:
        form = Bibliografia_form(request.POST)
        if form.is_valid():
            new_biblio = Bibliografia.objects.create(
                nombre_biblio = form.cleaned_data['nombre_biblio'],
                autor_biblio = form.cleaned_data['autor_biblio']
            )
            context = {'new_biblio':new_biblio}
        return render(request,'cargar_biblio.html',context=context)