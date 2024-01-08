from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blog

# Create your views here.
def Home(request):
    return render(request, "home.html")

def About(request):
    return render(request, "about.html")
def portfolio(request):
    return render(request, "portfolio.html")

def blog_detail(request):
    return render(request, "blog_detail.html")

def portfolio_detail(request):
    return render(request, "portfolio_detail.html")


def Blogs(request):
    posts=Blog.objects.all()
    context={
        'posts':posts
    }
    
    return render(request, "blog.html", context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        numb=request.POST.get('numb')
        descrip=request.POST.get('descrip')
        mycontact=Contact(name=name,email=email,number=numb,description=descrip)
        mycontact.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    return render(request, "contact.html")