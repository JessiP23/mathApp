from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#user must be logged to access the home page
@login_required(login_url='login')
def HomePage(request):
    username = request.user.username
    context = {'username': username}
    return render (request,'home.html', context)

#Authentication User
#form is submitted via POST method get username, email, passwords
def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        initialpassword=request.POST.get('initialpassword')
        confirmpassword=request.POST.get('confirmpassword')

        if initialpassword != confirmpassword:
            return HttpResponse("Not the same password!")
        else:
            #create new user and save it
            new_user=User.objects.create_user(username,email,initialpassword)
            new_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        #asks for username in database
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        #authenticate user
        user=authenticate(request,username=username,password=pass1)

        if user is not None:
            #if user is correct and redirect the home page
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Classes_view(request):
    return render(request, 'classes.html')

def Sessions_view(request):
    return render(request, 'sessions.html')

def Post_view(request):
    return render(request, 'forum.html')

def ma010(request):
    return render(request, 'classes/ma010.html')

def ma025(request):
    return render(request, 'classes/ma025.html')

def precalculus(request):
    return render(request, 'classes/precalculus.html')

def calculusI(request):
    return render(request, 'classes/calculusI.html')

def calculusII(request):
    return render(request, 'classes/calculusII.html')

def calculusIII(request):
    return render(request, 'classes/calculusIII.html')

def differential_equations(request):
    return render(request, 'classes/differential_equations.html')