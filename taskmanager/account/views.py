from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .models import User

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('/')
 
    return render(request, 'account/signin.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('User created:', user)

            return redirect('/signin/')

        else:
            print('something went wrong')
    else:
        print('Just Form')
        
    return render(request, 'account/signup.html')

