from django.shortcuts import render , redirect
from django.contrib import auth
from django.http import HttpResponse
from .models import Student_Data_Row
from django.contrib.auth.models import User

# Create your views here.
def home (request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request ,'index.html')
     
    return redirect("loginin")
    
def school_manage (request):
    if request.method == 'GET':
        return render(request ,'school_management.html')
    
    
def student(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            items = Student_Data_Row.objects.all()
            return render (request,'student.html',{'items':items})
        
    
        
    
            
           
                
            
    
def loginin(request):
    if request.method == "GET":
        return render (request,'login.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request , username = username,password= password)
        if user:
            auth.login(request,user)
            return redirect('home')
        
        return HttpResponse("not match username and password")
    
def delete(request,id):
    if request.method == "GET":
        item_delete = Student_Data_Row.objects.get(pk=id)
        item_delete.delete()
    return redirect('student')    


        
def logout (request):
    if request.method == "GET":
        auth.logout(request)
        
    
    return redirect ('loginin')


def registration(request):
    if request.method == "GET":
        return render(request,'Registrations.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password == cpassword :
            user = User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
            user.save()
            return HttpResponse("<h1> one create user save please chek ..</h1>")
        
        return HttpResponse("please confrom the password ..!")
        



def add_student(request):
    if request.method == "GET":
        items = Student_Data_Row.objects.all() 
        return render (request,'add_student.html',{'items': items})
    
    if request.method == "POST":
        user = Student_Data_Row()
        
        user.row_number = request.POST.get('student_row_no')
        user.name = request.POST.get('student_name')
        user.age = request.POST.get('student_age')
        user.grade = request.POST.get('student_class') 
        
        user.save()
        return redirect ('student')
    
    return HttpResponse ("issue please cheak your data plain")


def all_teacher(request):
    if request.method == "GET":
        return render(request,'teacher.html')
    