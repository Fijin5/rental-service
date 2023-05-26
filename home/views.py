from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import booking,HomeEnquiry,HomeHomechoose
# Create your views here.
def index(request):

    return render(request,'home.html')
def home(request):
    if request.method == "POST":
        where=request.POST["where"]
        when=request.POST["when"]
        bookform=HomeHomechoose(here=where,hen=when)
        bookform.save()

    return render(request,'home.html')
def login(request):
    if request.method == "POST":
       username=request.POST["username"]
       password=request.POST["password"]
       user=authenticate(username=username,password=password)
       if  user is not None:
           request.session['username']=username
           return redirect('bookings2')
       else:
         return redirect('signup')
    return render(request,'login.html')
def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Already Exist')
                 return redirect('signup')
            else:
                myuser=User.objects.create_user(username=username,password=password1,email=email)
                myuser.save();
                print("user created")
                return redirect('login')
        else:
            print('password not matching..')
            return redirect('signup')
    else:  
      return render(request,'signup.html')
def bookings(request):
      book = booking.objects.all

      return render(request,'bookings.html',{'book':book})

def bookings2(request):
    return render(request,'bookings2.html')
def contact(request):
    
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')


def enquiry(request):
    if request.method =="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        textarea=request.POST['textarea']
        enq=HomeEnquiry(fname=fname,lname=lname,email=email,mobile=mobile,textarea=textarea)
        enq.save();
    return render(request,'contact.html')