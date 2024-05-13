from django.shortcuts import render,redirect
from .models import Employee
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def insertData(request):
    data=Employee.objects.all()
    print(data)
    context={"data":data}
    print(context)

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Employee(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/insert")
    return render(request,"index.html",context)

def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        edit=Employee.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/insert")

    d=Employee.objects.get(id=id)
    context={"d":d}

    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("/insert")

def about(request):
    return render(request,"about.html")
