from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from . models import movie
# Create your views here.
def index(request):
    mov=movie.objects.all()
    context={
        'movie_list':mov
    }
    return render(request,"index.html", context)

def detail(request,m_id):
    move=movie.objects.get(id=m_id)
    return render(request,'detail.html',{'move':move})

def add_mov(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        move=movie(name=name, desc=desc, year=year, img=img)
        move.save()
    return render(request,"addmov.html")
def update(request,id):
    move=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES, instance=move)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'move':move})

def delete(request,id):
    if request.method=='POST':
        move=movie.objects.get(id=id)
        move.delete()
        return redirect('/')
    return render(request,'delete.html')