from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contacts
from .tasks import send_mails
from django_celery_beat.models import PeriodicTask,CrontabSchedule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
def index(request):
  if request.user.is_authenticated:
      return render(request,"index.html")

  else:
       return redirect("Login")

def contacts(request):
  if request.user.is_authenticated:
    if request.method=='POST':
      username=request.POST.get("username")
      desc=request.POST.get("desc")
      contact=Contacts(username=username,desc=desc)
      contact.save()
      messages.success(request, "Profile details updated.")

    return render(request,"contact.html")
  else:
       return redirect("Login")

def signup(request):
    if request.method=='POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       email=request.POST.get("email")
       user = User.objects.create_user(username, email, password)
       authenticate(request, username=username, password=password)
       user.save()
       send_mails.delay()
       return redirect('index')

    return render(request,"signup.html")

def Login(request):

   if request.user.is_authenticated:
        return redirect("index")
   if request.method=='POST':
       username = request.POST.get("username")
       password = request.POST.get("password")

       user=authenticate(request, username=username, password=password)
       if user is not None:            
            login(request, user)
            return redirect("index")
         
       else:

            return redirect("index")
    
   return render(request,"login.html")
 

def Logout(request):
    logout(request)
    return redirect('Login')


@login_required
@permission_required('home.can_add_data')
def sendmails(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=9,minute=14)
    task=PeriodicTask.objects.create(crontab=schedule,name="send_mail_anishshi",task='home.tasks.send_mail1')
    return render(request,"index.html")
