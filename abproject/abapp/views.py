from django.shortcuts import render,redirect
from abapp.models import emp1,emp2
from abapp.form import empform,loginform

# Create your views here.
def aaa(request):
    if request.method=="POST":
        form=empform(request.POST)
        if form.is_valid():
            try:
                form.save()
                msg="file uploaded sucessfully"
                return render(request,'bbb.html',{'msg':msg})
            except:
                msg="error"
                return render(request,'bbb.html',{'msg':msg})
        else:
            form=empform()
            msg="error"
            return render(request,"aaa.html",{'form':form,'msg':msg})
    else:
        form=empform()
        return render(request,"aaa.html",{'form':form})
    
def view(request):
    a=emp1.objects.all()
    return render(request,'ccc.html',{'a':a})

def edit(request,id):
    a=emp1.objects.get(id=id)
    return render(request,'ddd.html',{'a':a})

def update(request,id):
    if request.method=="POST":
        a=emp1.objects.get(id=id)
        form=empform(request.POST,instance=a)
        if form.is_valid():
            try:
                form.save()
                msg="file updated sucessfully"
                return render(request,'bbb.html',{'msg':msg})
            except:
                msg="error"
                return render(request,'bbb.html',{'msg':msg})
def delete(request,id):
    a=emp1.objects.get(id=id)
    a.delete()
    return redirect('/view')

def register(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                msg="file uploaded sucessfully"
                return render(request,'register.html',{'msg':msg})
            except:
                msg="error"
                return render(request,'register.html',{'msg':msg})
        else:
            form=loginform()
            msg="error"
            return render(request,"register.html",{'form':form,'msg':msg})
    else:
        form=loginform()
        return render(request,"register.html",{'form':form})
