"""
URL configuration for project_juju project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_management import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.SignUpPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('registration/', views.RegistrationPage, name='regitser'),
    path('recc/', views.RecommendationPage, name='recommendation'),
    path('forgot/', views.ForgotPage, name='forgot'),
    path('cursed/', views.CursedPage, name='cursed'),
    path('authors/', views.AuthorPage, name='authors'),
    path('discover/', views.DiscoverPage, name='discover'),
    path('thrones/', views.thrones, name='thrones'),
    path('page1', views.page1, name='page1'),
    path('page2', views.page2, name='page2'),
    path('page3', views.page3, name='page3'),
    path('page4', views.page4, name='page4'),
    path('page5', views.page5, name='page5'),
    path('page6', views.page6, name='page6'),
    path('page7', views.page7, name='page7'),
    path('page8', views.page8, name='page8'),
    path('page9', views.page9, name='page9'),
    path('page10', views.page10, name='page10'),
    path('page11', views.page11, name='page11'),
    path('page12', views.page12, name='page12'),
    path('page13', views.page13, name='page13'),
    path('page14', views.page14, name='page14'),
    path('page15', views.page15, name='page15'),
    path('page16', views.page16, name='page16'),
    path('page18', views.page18, name='page18'),
    path('page19', views.page19, name='page19'),
    path('page20', views.page20, name='page20'),
    path('page21', views.page21, name='page21'),
    path('page22', views.page22, name='page22'),
    path('page23', views.page23, name='page23'),
    path('page24', views.page24, name='page24'),
    path('page25', views.page25, name='page25'),
    path('page26', views.page26, name='page26'),
    path('page27', views.page27, name='page27'),
    path('end', views.end, name='end'),


    




   ]