# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User, Trip
from django.contrib import messages
# Create your views here.

def dashboard(request):
    if 'user_name' not in request.session:
        return redirect('/')
    
    
    context = {
        'cur_user': User.objects.get(id = request.session['id']),
        'trips': Trip.objects.all(),
    
    }
    return render(request, 'main_app/dashboard.html', context)


def addtrip(request):
    if 'user_name' not in request.session:
        return redirect('/')
    return render(request, 'main_app/addtrip.html')

def createtrip(request):
    Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], trip_planner=request.session['first_name'], start_date=request.POST['start_date'], end_date=request.POST['end_date'])
    return redirect ('/main/dashboard')


def jointrip(request, id):
    logged_user=User.objects.get(id=request.session['id'])
    trip=Trip.objects.get(id=id)
    logged_user.traveler.add(trip)
    return redirect ('/main/dashboard')
    

def logout(request):
    request.session.flush()
    return redirect ('/')


def show(request, id):
    
    context = {
        'destination': Trip.objects.get(id=id),
        'other_travelers': Trip.objects.all()
    }
    return render(request, 'main_app/show.html',context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    