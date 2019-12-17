from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Successfully Logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfully Log out!")
        return redirect('login')

def register(request):
    if request.method == 'POST':
        #Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Checking Password Match
        if password == password2:
            #username
            if User.objects.filter(username=username).exists():
                messages.ERROR(request, "that username already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.ERROR(request,"Email is already being used")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                    # Login after Register
                    # auth.login(request,user)
                    # messages.success(request, "Successfully logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request, "You'are successfully registered")
                    return redirect('register')
            return
        else:
            messages.ERROR(request, "Password didn't match")
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    #first_name = request.POST['first_name']
    #last_name = request.POST['last_name']
    return render(request, 'accounts/dashboard.html')
