from django.shortcuts import render,redirect
from .models import stdModel


def frontpage(request):
    Recstd=stdModel.objects.all()
    return render(request,'index.html',{'record':Recstd})


def Create(request):
    return render(request,'create.html')
def Addstd(request):
    x=request.POST['first']
    y=request.POST['last']
    crt=stdModel(firstname=x,lastname=y)
    crt.save()
    return redirect('/')

def Update(request,id):
    upd=stdModel.objects.get(id=id)
    return render(request,'update.html',{'upd':upd})

def recUpdate(request,id):
    reupd=stdModel.objects.get(id=id)
    x=request.POST['first']
    y=request.POST['last']
    reupd.firstname=x
    reupd.lastname=y
    reupd.save()
    return redirect("/")


def Delete(request,id):
    del1=stdModel.objects.get(id=id)
    del1.delete()
    return redirect('/')

# Create your views here.
