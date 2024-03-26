from django.shortcuts import render,HttpResponse,redirect
from .models import CrudApp
from django.contrib import messages

# Create your views here.

def index(request): 
    data = CrudApp.objects.all()   
    context = {
        "title":"Home",
        "data":data,
           }
    return render(request, "core/index.html",context)
def insertData(request):
    data = CrudApp.objects.all() 
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        # print(f'My name is ${name} and age is ${age}.Your mail is ${email} and your gender is ${gender}')
        query = CrudApp(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.success(request,"Student Added Successfully")
        return redirect('/')
    context = {
        "title":"Insert Data",
        "data":data,
       
           }
    return render(request, "core/index.html",context)

def updateData(request,id): 
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        edit = CrudApp.objects.get(id=id) 
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        messages.warning(request,"Student Updated Successfully")
        return redirect('/')  
    data = CrudApp.objects.get(id=id) 
    context = {
        "title":"Home",
        "data":data,
        
           }
    return render(request, "core/update.html",context)
def deleteData(request,id): 
    data = CrudApp.objects.get(id=id)  
    data.delete()
    messages.warning(request,"Student Deleted Successfully") 
   
    return redirect('/')
    