from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from homeapp.forms import userform, LoginRegister, workerform


# Create your views here.
def mainpage(request):
    return render(request,'index1.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_user:
                return redirect('user')
            elif user.is_worker:
                return redirect('worker')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def adminpage(request):
    return render(request,'inindexadm.html')

def user(request):
    return render(request,'user.html')

def worker(request):
    return render(request,'worker.html')

def userregister(request):
    user_form=LoginRegister()
    userregister_form=userform()
    if request.method=='POST':
        user_form=LoginRegister(request.POST)
        userregister_form=userform(request.POST,request.FILES)
        if user_form.is_valid()and userregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_user=True
            user.save()
            userregister=userregister_form.save(commit=False)
            userregister.user=user
            userregister.save()
            messages.info(request,'Registration Successfully')
            return redirect('loginpage')
    return render(request,'userregister.html',{'user_form':user_form,'userregister_form':userregister_form})


def workerregister(request):
    user_form = LoginRegister()
    workerregister_form=workerform()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        workerregister_form=workerform(request.POST,request.FILES)
        if user_form.is_valid() and workerregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_user = True
            user.save()
            workerregister=workerregister_form.save(commit=False)
            workerregister.user = user
            workerregister.save()
            messages.info(request, 'Registration Successfully')
            return redirect('loginpage')
    return render(request,'workerregister.html',{'worker_form':user_form,'workerregister_form':workerregister_form})


