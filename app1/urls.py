from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.load_current_user_info, name="sample"),
    path('register/', views.register, name="register"),
    path('login/', views.my_login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('aboutus/', views.sample,name="knowaboutus"),
    path('userinfo/', views.userinfo, name="userinfo"),
    path('inbox/', views.inbox, name="inbox"),
    path('info/', views.load_current_user_info, name="currentdata"),
    path('edit/', views.patch_user_info, name="patch"),
    path('discover/', views.discover_page, name="discover"),
    path('discover/single/', views.discover_single, name="single"),
    path('discover/longdistance/', views.discover_long_distance, name="longdistance"),
    path('discover/taken/', views.discover_dating, name="dating"),
    path('discover/mechanical/', views.discover_mechanical, name="mechanical"),
    path('discover/electrical/', views.discover_electrical, name="electrical"),
    path('discover/GPT/', views.discover_GPT, name="GPT"),
    path('discover/GT/', views.discover_GT, name="GT"),
    path('discover/electronics/', views.discover_electronics, name="electronics"),
    path('discover/eph/', views.discover_eph, name="eph"),
    path('discover/cse/', views.discover_cse, name="cse"),
    path('discover/economics/', views.discover_economics, name="economics"),
    path('discover/civil/', views.discover_civil, name="civil"),
    path('discover/architecture/', views.discover_architecture, name="architecture"),
    path('discover/DSAI/', views.discover_dsai, name="DSAI"),
    path('discover/mnc/', views.discover_mnc, name="mnc"),
    path('discover/chemicalscience/', views.discover_cs, name="cs"),
    path('discover/chemicalengineering/', views.discover_chemical, name="chemical"),
    path('discover/metallurgy/', views.discover_metallurgy, name="metallurgy"),
    path('discover/pni/', views.discover_pni, name="pni"),
    path('discover/biotech', views.discover_biotech,name="biotech"),
    
    
    #----------------------------------------------------X----------------------------------------------------------
    
    
    path('discover/male/', views.discover_male, name="male"),
    path('discover/female/', views.discover_female, name="female"),
    path('discover/rather/', views.discover_rather, name="rather"),

    path('check/', views.logic, name = "logic"),
    

]
