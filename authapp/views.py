from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from authapp.forms import Edit_Registration
from django.contrib.auth.views import PasswordChangeForm

# Create your views here.
def Register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            messages.info(request,"Your Password not incorrect!")
            return redirect('/authapp/register')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Username is Taken")
                return redirect('/authapp/register')
        except Exception as identifier:
            pass    
        else:   
            myuser=User.objects.create_user(username,email,password1)
            myuser.save()
            messages.success(request,"User is Created Please Login")
            return redirect('login')
        
        
    return render(request, 'authapp/register.html')


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('/')
            
        else:
            messages.error(request,"Username or Password is incorrect!!!")
           
    return render(request, 'authapp/login.html')

def Logout(request):
    logout(request)
    messages.success(request,"logout Successfully")
    return render(request, 'authapp/login.html')

def edit_registration(request):
    if request.method == 'POST':  
        form = Edit_Registration(request.POST, instance=request.user)  
        if form.is_valid():  
            form.save() 
            messages.success(request, 'Account Updated successfully') 
            return redirect('/') 
  
    else:  
        form = Edit_Registration(instance=request.user)  
    context = {  
        'form':form  
    } 
    return render(request, 'authapp/edit_registration.html',context)

def change_password(request):
    if request.method == 'POST':  
        form = PasswordChangeForm(data=request.POST, user=request.user)  
        if form.is_valid():  
            form.save() 
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Change Password successfully') 
            return redirect('/') 
  
    else:  
        form = PasswordChangeForm(user=request.user)  
    context = {  
        'form':form  
    } 
    return render(request, 'authapp/change_password.html',context)