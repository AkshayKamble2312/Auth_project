from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

#password Prashant@143

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def registeruser(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return redirect('/registeruser')
            else:
                u_info=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                u_info.save()
                return redirect('/login')

def loginuser(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')
            
        
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")