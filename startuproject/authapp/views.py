from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def handlesignup(request):
    flag = 0
    if request.method=="POST":
        name = request.POST["name"]
        email =  request.POST["email"]
        password = request.POST["password"]
        confrm_passwrd = request.POST["confirm-password"]
        # print(name,email,password,confrm_passwrd)


        if password != confrm_passwrd:
            messages.warning(request, "Password is not matching")
            return redirect('/authapp/signup/')
            
        if len(password) < 8:
            messages.warning(request, "Password must be at least 8 characters")
            return redirect('/authapp/signup/')
            
        if not re.search("[a-z]", password):
            flag = -1

        elif not re.search("[A-Z]", password):
            flag = -1

        elif not re.search("[0-9]", password):
            flag = -1

        elif not re.search("[_@#$%^&*()-]", password):
            flag = -1

        else:
            pass

        if flag == -1:
            messages.warning(request, "Password must contain lowercase, uppercase, digit, and special character")
            return redirect('/authapp/signup/')
        if(flag==0):
            try:
                if User.objects.get(username=email):
                    messages.info(request,"Email is Taken")
                    return redirect('/authapp/signup/')
                
            except Exception as identifier:
                pass
            user = User.objects.create_user(email,email,password)
            user.first_name=name
            # user.is_active=False
            user.save()

        messages.success(request, "Signup Success please login")
        return redirect('/authapp/login/')
    
    return render(request, 'signup.html')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['password']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request, "Login Successfully")
            return redirect('/')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/authapp/login/')
        
    return render(request, "login.html")



def handleLogout(request):
    logout(request)
    messages.success(request, "Loged Out Succesfully♫")
    return render(request, "login.html")