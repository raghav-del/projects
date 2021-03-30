from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['name'].split()[0]
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.filter(username=username)
            if user.exists():
                messages.error(request, 'User already exists')
            else:
                new_user = User.objects.create_user(username=username, 
                                                password=password, email=email,first_name=first_name)
                auth.login(request,new_user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords dont match')
            
            
    
    return render(request,'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print('print00000000000000000')
            auth.login(request,user)
            return redirect('home')
        else:
            print('ye galat hai')
            messages.error(request,'Invalid Credentials')
        
    return render(request,'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
