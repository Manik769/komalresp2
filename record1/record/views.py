
from django.shortcuts import render, redirect,HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    username=request.POST['username']
    password=request.POST['password']
    if username=="manik" and password=="123":
        return render(request,'output.html')
    else:
        return render(request, 'index.html')
def login1(request):
    return render(request,'company.html')
def login2(request):
    return render(request,'employee.html')
def login3(request):
    return render(request,'employee.html')
def login4(request):
    return render(request,'employee.html')
def login5(request):
    return render(request,'index.html')

def cmp(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/details")
            except:
                pass
    else:
        form=UserForm()
    return render(request,'company.html',{'form':form})
def details(request):
    userData=User.objects.all()
    return render(request,"details.html",{'userData':userData})

def edit(request,id):
    userData = User.objects.get(id=id)
    return render(request, "edit.html", {'userData': userData})

def update(request,id):
    userData = User.objects.get(id=id)
    form=UserForm( request.POST,instance=userData)
    if form.is_valid():
        form.save()
        return redirect("/details")
    return render(request,'edit.html',{'userData':userData})

def delete(request,id):
    userData = User.objects.get(id=id)
    userData.delete()
    return redirect("/details")










