from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def RecommendationPage(request):
    return render(request, 'recommendations.html')

def RegistrationPage(request):
    return render(request, 'registration.html')

def ForgotPage(request):
    return render(request, 'forgotpassword.html')

def CursedPage(request):
    return render(request, 'curseddreams.html')

def AuthorPage(request):
    return render(request, 'authors.html')

def DiscoverPage(request):
    return render(request, 'discover.html')

def thrones(request):
    return render(request, 'thrones.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')


def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')


def page5(request):
    return render(request, 'page5.html')

def page6(request):
    return render(request, 'page6.html')

def page7(request):
    return render(request, 'page7.html')

def page8(request):
    return render(request, 'page8.html')

def page9(request):
    return render(request, 'page9.html')

def page10(request):
    return render(request, 'page10.html')

def page11(request):
    return render(request, 'page11.html')

def page12(request):
    return render(request, 'page12.html')

def page13(request):
    return render(request, 'page13.html')

def page14(request):
    return render(request, 'page14.html')

def page15(request):
    return render(request, 'page15.html')

def page16(request):
    return render(request, 'page16.html')

def page18(request):
    return render(request, 'page18.html')

def page19(request):
    return render(request, 'page19.html')

def page20(request):
    return render(request, 'page20.html')

def page21(request):
    return render(request, 'page21.html')

def page22(request):
    return render(request, 'page22.html')

def page23(request):
    return render(request, 'page23.html')

def page24(request):
    return render(request, 'page24.html')

def page25(request):
    return render(request, 'page25.html')


def page26(request):
    return render(request, 'page26.html')

def page27(request):
    return render(request, 'page27.html')

def end(request):
    return render(request, 'TheEnd.html')













def SignUpPage(request):
    if request.method =="POST":
        uname = request.POST.get('username') 
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        my_user = User.objects.create_user(uname, email,password1)
        my_user.save()
        return redirect('login')

        
    return render(request ,'registration.html')


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user= authenticate(request, username = username, password = password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ("username or password is incorrect")

    return render(request ,'Login1.html')