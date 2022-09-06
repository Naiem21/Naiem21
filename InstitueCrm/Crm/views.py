from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import redirect,render
from .models import Admin, Subject

# Create your views here.
def openLoginForm(request):
    if request.session.get('adminid'):
        return render(request,"Dashboard.html");
    else:
        return render(request,"Login.html")

def login(request):
    phone=request.POST['phone']
    password=request.POST['password']
    result=Admin.objects.filter(phone=phone,password=password)
    if result:
        dataList=result.values()
        request.session['adminid']=dataList[0]['id']
        return redirect("/dashboard")
    else:
        return render(request,"Login.html",{"error": "Invalid phone number or password "})

def logout(request):
    del request.session['adminid']
    return redirect("/")

def openDashboard(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid') 
        admin=Admin.objects.get(id=loggedInAdminId)
        return render(request,"Dashboard.html",{"admin":admin});
    else:
        return redirect("/")

def openSubjectForm(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        return render(request,"SubjectForm.html",{"admin":admin});
    else:
        return redirect("/")
    
def openSubjectslist(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid') 
        admin=Admin.objects.get(id=loggedInAdminId)
        Subjects=Subject.objects.all()
        return render(request,"ViewSubjects.html",{"subjects":Subjects,"admin":admin});
    else:
        return redirect("/")

def addSubject(request):
    subject= Subject()
    subject.name=request.POST['name'];
    subject.description=request.POST['description']
    subject.save();
    return HTTPResponse("subject inserted!!")

def deleteSubject(request, id):
    subject= Subject.objects.get(id=id)
    subject.delete();
    return redirect("/fetchall")


def updateSubject(request, id):
    subject = Subject.objects.get(id=id)
    subject .name=request.POST['name']
    subject .save()
    return redirect("/fetchall")


def openEditForm(request,id):
    subject= Subject.objects.get(id=id)
    return render(request,"SubjectFrom.html",{"Subject":subject})
     