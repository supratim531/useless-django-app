from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from final.models import Contact
from datetime import datetime

# Create your views here.
GlobalUserName = "admin"
def index(request):
    dec = False
    context = {'dec':dec, 'Name':request.user}
    if request.user.is_anonymous:
        pass
    else:
        dec = True
        context = {'dec':dec, 'Name':request.user}
        messages.success(request, "You are logged in to our Avengers portal")
        return render(request, "index.html", context)
    return render(request, "index.html", context)

def about(request):
    if request.user.is_anonymous:
        messages.warning(request, "You are not logged in! To see About you have to login first")
        return redirect("/")
    return HttpResponse("<p style='font-family:Fira Code;'>Can not get about.html Http error 404 not found!</p>")

def contact(request):
    if request.user.is_anonymous: return redirect("/login/")
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact_object = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact_object.save()
        context = {
            'Name':name
        }
        messages.success(request, "Your details submitted successfully")
        return render(request, "contact.html", context)
    return render(request, "contact.html")

def services(request):
    if request.user.is_anonymous:
        messages.warning(request, "You are not logged in! To see Services you have to login first")
        return redirect("/")
    return HttpResponse("<p style='font-family:Fira Code;'>Can not get services.html Http error 404 not found!</p>")

def loginUser(request):
    global GlobalUserName
    context = {'Name':GlobalUserName}
    if request.method == 'POST':
        password = request.POST.get('pwd')
        username = request.POST.get('uname')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context = {
                'Name':username
            }
            messages.warning(request, "it seems either wrong password or you are not registered in our Avengers portal!")
            return render(request, "login.html", context)
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("/login/")

def signup(request):
    if request.method == 'POST':
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        global GlobalUserName
        GlobalUserName = username
        if pass1 != pass2:
            messages.warning(request, "Password did not match!")
            return redirect("/login/")
        if not username.isalnum():
            messages.warning(request, "Username should only contain letters and numbers!")
            return redirect("/login/")
        newUser = User.objects.create_user(username, email, pass1)
        newUser.first_name = fname
        newUser.last_name = lname
        newUser.save()
        messages.success(request, "Your account has been successfully registered! Now you can login in our Portal")
        return redirect("/login/")
    else:
        return redirect("/login/")
