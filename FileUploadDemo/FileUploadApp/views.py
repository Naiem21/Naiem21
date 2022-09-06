from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def openForm(request):
    form=UserForm()
    return render(request,"Form.html",{"form":form})

def registerUser(request):
    form=UserForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("user registered!")
    else:
        return HttpResponse("registration failed!")
    
def deleteUser(request):
    form=UserForm(request.POST,request.FILES)
    