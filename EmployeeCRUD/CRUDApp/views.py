from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
# Create your views here.

def openForm(request):
    return render(request,"form.html")

def saveEmployee(request):
    emp=Employee()
    emp.name=request.POST['name']
    emp.salary=request.POST['salary']
    emp.phone=request.POST['phone']
    emp.gender=request.POST['gender']
    emp.dob=request.POST['dob']
    emp.save()
    return redirect("/fetchall")

def getAllEmployees(request):
    employeesList=Employee.objects.all()
    return render(request,"show.html",{"employees":employeesList})

def deleteEmployee(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect("/fetchall")

def updateEmployee(request,id):
    emp=Employee.objects.get(id=id)
    emp.name=request.POST['name']
    emp.salary=request.POST['salary']
    emp.phone=request.POST['phone']
    emp.gender=request.POST['gender']
    emp.dob=request.POST['dob']
    emp.save()
    return redirect("/fetchall")

def openEditForm(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,"updateform.html",{"employee":emp})